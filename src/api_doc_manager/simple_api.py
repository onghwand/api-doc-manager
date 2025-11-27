from fastapi import FastAPI

app = FastAPI()

@app.get("/hello1234")
def read_root(param: str, param2: str):
    """
    Simple API that accepts one parameter and returns 'hello'.
    """
    return "hello"
