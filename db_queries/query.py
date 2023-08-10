from mock_db import mock_db
from uuid import uuid4


def add_to_db(todo):
    to_add = todo.dict()
    to_add["id"] = str(uuid4())
    to_add["is_close"] = False
    mock_db.append(to_add)
    return to_add


def get_one_todo(todo_id):
    for todo in mock_db:
        t_id = todo.get("id")
        if t_id == todo_id:
            return todo
    return None


def update_one_todo(t_id, new_colums):
    to_update = get_one_todo(t_id)
    for key, value in new_colums.items():
        to_update[key] = value
    return None


def delete_from_mock_db(t_id):
    to_delete = get_one_todo(t_id)
    mock_db.remove(to_delete)
    return None
