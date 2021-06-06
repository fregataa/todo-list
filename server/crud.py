import sqlalchemy as sa
from typing import List

# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import models, schemas


async def get_all_user(db: AsyncSession) -> List[models.User]:
    stmt = select(models.User)
    query = await db.scalar(stmt)
    return query


# def get_user_by_email(db: Database, email: str):
#     # query = sa.select()
#     return db.query(models.User).filter(models.User.email == email).first()

# def create_user(db: Database, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email,
#                           hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_todos(db: Database, skip: int = 0, limit: int = 100):
#     return db.query(models.Todo).offset(skip).limit(limit).all()

# def create_user_todo(db: Database, todo: schemas.TodoCreate, user_id: int):
#     db_todo = models.Todo(**todo.dict(), owner_id=user_id)
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo
