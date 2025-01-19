from fastapi import APIRouter

router2 = APIRouter(prefix='/user', tags=['user'])


@router2.get('/')
async def all_users():
    pass


@router2.get('/user_id')
async def user_by_id():
    pass


@router2.post('/create')
async def user_create():
    pass


@router2.put('/update')
async def user_update():
    pass


@router2.delete('/delete')
async def user_delete():
    pass
