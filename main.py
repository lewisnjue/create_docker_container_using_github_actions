from fastapi import FastAPI 

app = FastAPI()


@app.get('/')
async def hello_home():
    return {"messange":"hello world"}