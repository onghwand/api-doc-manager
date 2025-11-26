from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root(param: str):
    """
    Simple API that accepts one parameter and returns 'hello'.
    """
    return "hello"
