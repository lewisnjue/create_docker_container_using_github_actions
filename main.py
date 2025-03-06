from fastapi import FastAPI 

app = FastAPI()


@app.get('/')
async def hello_home():
    return {"messange":"hello world"}

@app.get('/hello')
async def hello_hello():
    return {"messange":"hello again"}