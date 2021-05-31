from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import db, User, Good,CartRecord

app = FastAPI()

# 设置跨域允许
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


@app.get('/login')
async def login(username: str = "", password: str = ""):
    success = False
    exist = False
    name = ""
    for user in db.users.find({"username": username}):
        exist = True
    for user in db.users.find({"username": username, "password": password}):
        success = True
        name = User(**user).name
    return {'success': success, "exist": exist, "name": name}


@app.get('/getGood')
async def get_good(g_no: str = "1"):
    good = ""
    for g in db.goods.find({"g_no": g_no}):
        good = Good(**g)
    # goods.append(Good(*good))
    return good

#查询购物车
@app.get('/getCartGood')
async def get_cart_good(page: int = 1, size: int = 1):
    skip = size * (page - 1)
    dataCount = db.cart.find().count()
    goods = []
    for g in db.cart.find().limit(size).skip(skip):
        goods.append(CartRecord(**g))
    # goods.append(Good(*good))
    return {'data': goods, 'data_count': dataCount}

#查询商品列表
@app.get('/getGoodList')
async def get_good_list(page: int = 1, size: int = 1):
    skip = size * (page - 1)
    dataCount = db.goods.find().count()
    goodList = []
    for g in db.goods.find({},{"_id":0,"g_no":1}).limit(size).skip(skip):
        print(type(g))
        print(g)
        goodList.append(g["g_no"])
    # goods.append(Good(*good))
    return {'data': goodList, 'data_count': dataCount}


@app.get('/addCart')
async def add_cart(g_no: str = "1", num: int = 1):
    #查找商品
    good = ""
    for g in db.goods.find({"g_no": g_no}):
        good = Good(**g)
    record = ""
    for r in db.cart.find({"g_no": good.g_no}):
        record = CartRecord(**r)
    if record:
        db.cart.update({"g_no":record.g_no},{"$set":{"num":record.num+num}})
    else:
        record = {}
        record["g_name"] = good.g_name
        record["g_no"] = good.g_no
        record["price"] = good.price
        record["num"] = num
        print(record)
        db.cart.insert_one(record)
    # goods.append(Good(*good))
    return {"success":True}

@app.get('/updateCart')
async def update_cart(g_no: str = "1", num: int = 1):
    #查找商品
    good = ""
    for g in db.goods.find({"g_no": g_no}):
        good = Good(**g)
    record = ""
    for r in db.cart.find({"g_no": good.g_no}):
        record = CartRecord(**r)
    if record:
        db.cart.update({"g_no":record.g_no},{"$set":{"num":num}})
    else:
        record = {}
        record["g_name"] = good.g_name
        record["g_no"] = good.g_no
        record["price"] = good.price
        record["num"] = num
        print(record)
        db.cart.insert_one(record)
    # goods.append(Good(*good))
    return {"success":True}

@app.get('/removeCart')
async def remove_cart(g_no: str = "1"):
    #查找记录
    record = ""
    for r in db.cart.find({"g_no": g_no}):
        record = CartRecord(**r)
    if record:
        db.cart.delete_many({'g_no': g_no})
    # goods.append(Good(*good))
    return {"success":True}


@app.post('/createGood')
async def create_good(good: Good):
    if hasattr(good, 'id'):
        delattr(good, 'id')
    ret = db.goods.insert_one(good.dict(by_alias=True))
    good.id = ret.inserted_id
    return {'good': good}
