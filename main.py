import index,uvicorn

app = index.app

if __name__ == "__main__":
    # 使用 Uvicorn 启动 FastAPI 应用
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
