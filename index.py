from fastapi import FastAPI
from pydantic import BaseModel
import os
from typing import Optional

app = FastAPI()


# 定义请求体模型
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# GET 请求示例
@app.get("/")
async def root():
    return {"message": "Hello World"}

# POST 请求示例
@app.post("/items/")
async def create_item(item: Item):
    return item

# 动态路径参数
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
