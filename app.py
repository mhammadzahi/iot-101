from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/")
async def index(request: Request):
    return {"message": "Welcome to the IoT 101 API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True) # dev
    # uvicorn.run("app:app", host="0.0.0.0", port=8001) # prod

