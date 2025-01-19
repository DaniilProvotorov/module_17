from fastapi import APIRouter

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
