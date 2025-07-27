from fastapi import FastAPI, Request
import uvicorn


app = FastAPI()

@app.post("/api/v1/iot/101")
async def iot_101(request: Request):
    data = await request.json()
    # Process the data as needed
    return {"message": "Data received", "data": data}



@app.get("/")
async def index(request: Request):
    return {"message": "Welcome to the IoT 101 API"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True) # dev
    # uvicorn.run("app:app", host="0.0.0.0", port=8001) # prod
