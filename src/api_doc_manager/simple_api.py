from fastapi import FastAPI

app = FastAPI()

@app.get("/hello12")
def read_root(param: str):
    """
    Simple API that accepts one parameter and returns 'hello'.
    """
    return "hello"
