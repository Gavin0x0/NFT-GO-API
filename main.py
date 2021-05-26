from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import db, User, Good

app = FastAPI()

#设置跨域允许
origins = [
    "http://localhost:8080",
    "https://632891553.xyz",
    "https://nft.632891553.xyz",
    "https://www.632891553.xyz",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/users')
async def list_users():
    users = []
    for user in db.users.find():
        users.append(User(**user))
    return {'users': users}


@app.post('/users')
async def create_user(user: User):
    if hasattr(user, 'id'):
        delattr(user, 'id')
    ret = db.users.insert_one(user.dict(by_alias=True))
    user.id = ret.inserted_id
    return {'user': user}


@app.get('/getGood')
async def get_good(g_id: str = "1"):
    good = ""
    for g in db.goods.find({"g_no": g_id}):
        good = Good(**g)
    #goods.append(Good(*good))
    return good


@app.post('/createGood')
async def create_user(good: Good):
    if hasattr(good, 'id'):
        delattr(good, 'id')
    ret = db.goods.insert_one(good.dict(by_alias=True))
    good.id = ret.inserted_id
    return {'good': good}
