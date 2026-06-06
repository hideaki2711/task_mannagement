# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class TaskCreate(BaseModel):
#     user_id:str
#     task_index:str
#     deadline:str
#     priority:int
#     task_title:str
#     task_description:str

# @app.post("/api/tasks")
# def create_task(task:TaskCreate):
#     print("フロントエンドから情報が来ました。")
#     print(f"ユーザーID:{task.user_id}")
#     print(f"タスクの種類:{task.task_index}")
#     print(f"タスクの締め切り:{task.deadline}")
#     print(f"タスク名:{task.task_title}")
#     print(f"内容:{task.task_description}")

#     return{"status":"succsess","message":"タスクを作成しました","received_date":task}

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel

import detabase 
import models
import crud 

models.Base.metadata.create_all(bind=detabase.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskCreate(BaseModel):
    user_id:str
    task_index:str
    deadline:str
    priority:int
    task_title:str
    task_description:str


@app.post("/api/tasks")
def create_task(task:TaskCreate, db: Session = Depends(detabase.get_db)):
 print("フロントからデータが届きました。データを保存します。")
 db_task = crud.create_task_in_db(db=db, task_data=task)

 return {
    "status":"succcess",
    "message":"データベースに保存しました",
     "data" : {
       "id" : db_task.id,
       "user_id":db_task.user_id,
       "task_index":db_task.task_index,
       "deadline": db_task.deadline,
       "priority": db_task.priority,
       "task_title": db_task.task_title,
       "task_description": db_task.task_description
     }
   }

@app.get("/api/tasks")
def read_task(db: Session = Depends(detabase.get_db)):
    print("フロントからタスク一覧を出すようにリクエストあり")
    tasks = crud.get_all_tasks(db=db)

    return tasks

@app.delete("/api/tasks/{task?id}")
def delete_task(task_id: int, db:Session = Depends( detabase.get_db)):
  print("フロントからID:{task_id}の削除依頼がありました。")


  success = crud.delete_task_by_id(db=db, task_id=task_id)
  if not success:
     from fastapi import HTTPException
     raise HTTPException(status_code=404, datail="タスクが見つかりませんでした。")

  return{"message":"削除成功"} 