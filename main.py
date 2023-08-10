from fastapi import FastAPI, status
from schemas.todo import TodoItem, TodoResponse
from mock_db import mock_db
from db_queries.query import add_to_db, get_one_todo, update_one_todo, delete_from_mock_db


app = FastAPI()


@app.get("/todo", summary="Возвращает все таски", status_code=status.HTTP_200_OK)
async def all_todos():
    return mock_db


@app.post("/todo", summary="Записывает новую todo в \"БД\"", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoItem) -> TodoResponse:
    new_todo = add_to_db(todo)
    return new_todo


@app.get("/todo/{t_id}", status_code=status.HTTP_200_OK)
async def get_one(t_id: str):
    result = get_one_todo(t_id)
    return result


@app.patch("/todo/{t_id}", status_code=status.HTTP_200_OK)
async def update_todo(t_id: str, columns: dict):
    update_one_todo(t_id=t_id, new_colums=columns)
    return None


@app.delete("/todo/{t_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(t_id):
    delete_from_mock_db(t_id)
    return None
