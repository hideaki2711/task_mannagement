from sqlalchemy.orm import Session
import models

def create_task_in_db(db : Session, task_data):
    db_task =models.TaskModel(
        user_id = task_data.user_id,
        task_index = task_data.task_index,
        deadline = task_data.deadline,
        priority = task_data.priority,
        task_title = task_data.task_title,
        task_description = task_data.task_description
    )
    db.add (db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

#データベース全表示
def get_all_tasks(db: Session):
        return db.query(models.TaskModel).all()
    
# データベース削除
def delete_task_by_id(db: Session, task_id:int):
      db_task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
      if db_task:
           db.delete(db_task)
           db.commit()
           return True
      return False
