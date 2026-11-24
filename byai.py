from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def hello():
    return "jai hind"


@app.get("/about")
def homepage():
    return "this is home page"


@app.get("/users")
def get_users():
    return {"user": ["mohit", "ajay"]}


@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    return {"userid": user_id}


@app.get("/user")
def get_user_by_query(id: int | None = None):
    return {"name": id}


@app.get("/amozon")
def amozon(laptop: str | None = None, price: int | None = None):
    return {
        "laptopname": laptop,
        "laptopprice": price,
    }


BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008, "available": True},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2022, "available": True},
    {"id": 3, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999, "available": False},
    {"id": 4, "title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017, "available": True},
    {"id": 5, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019, "available": False},
]


@app.get("/books")
def get_books():
    return BOOKS


class User(BaseModel):
    name: str
    age: int


@app.post("/create_user")
def create_user(user: User):
    return {"data": user}


class Address(BaseModel):
    H_NO: int
    pincode: int
    landmark: str


class Information(BaseModel):
    name: str
    age: int
    id: int
    address: Address


@app.post("/user_information")
def user_information(data: Information):
    return {"this is user data": data}


class Todo(BaseModel):
    id: int
    task: str
    flag: bool


todos: list[Todo] = []


@app.post("/user_data")
def add_todo(temp: Todo):
    todos.append(temp)
    return {"inserted_data": temp}


@app.get("/todaytodo")
def user_today_todo():
    return todos