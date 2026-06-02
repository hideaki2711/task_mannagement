from sqlalchemy import Column, Integer, String
from detabase import Base 

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    task_index = Column(String, index=True)
    deadline = Column(String, index=True)
    priority = Column(Integer, index=True)
    task_title = Column(String, index=True)
    task_description = Column(String, index=True)