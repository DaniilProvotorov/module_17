
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import *
from app.shemas import CreateTask, UpdateTask
from sqlalchemy import insert, update, select, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_task(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(Task)).all()
    return users


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail='Task was not found')
    else:
        return task


@router.post('/create')
async def task_create(db: Annotated[Session, Depends(get_db)], ct: CreateTask, user_id):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    else:
        db.execute(insert(Task).values(title=ct.title,
                                       content=ct.content,
                                       priority=ct.priority,
                                       slug=slugify(ct.title),
                                       user_id=user_id))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def task_update(db: Annotated[Session, Depends(get_db)], ut: UpdateTask, task_id):
    task= db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail='Task was not found')
    else:
        db.execute(update(Task).where(Task.id == task_id).values(title=ut.title,
                                                                 content=ut.content,
                                                                 priority=ut.priority))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete('/delete')
async def task_delete(db: Annotated[Session, Depends(get_db)], task_id):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail='Task was not found')
    else:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful'}
