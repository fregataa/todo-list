from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import uvicorn

from .schemas import Todo

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/todos/", response_model=schemas.Todo)
def create_todo_for_user(user_id: int,
                         todo: schemas.TodoCreate,
                         db: Session = Depends(get_db)):
    return crud.create_user_todo(db=db, todo=todo, user_id=user_id)


@app.get("/todos/", response_model=List[schemas.Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos


# @app.get("/todos/{todo_id}")
# def read_todo(todo_id: int):
#     for _todo in todo_list:
#         if _todo.id != todo_id:
#             continue
#         return _todo
#     return {"No": "such todo"}

# @app.put("/todos/{todo_id}")
# async def put_todo(todo_id: int, todo: Todo):
#     todo_list.append(todo)
#     return {"todo_id": todo_id, **todo.dict()}

# @app.post("/todos/")
# async def post_todo(todo: Todo):
#     todo_list.append(todo)
#     return todo

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=5005,
                log_level="info",
                reload=True)
