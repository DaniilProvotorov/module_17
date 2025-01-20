
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task
from app.shemas import CreateTask, UpdateTask
from sqlalchemy import insert, update, select, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_task():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.post('/create')
async def task_create():
    pass


@router.put('/update')
async def task_update():
    pass


@router.delete('/delete')
async def task_delete():
    pass
