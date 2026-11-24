#lest build the fast api 

from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def hello():
    return "jai hind"

#home routes 
@app.get("/about")
def homepage():
    return "this is home page"

@app.get("/users")
def user():
    return {
        "user":['mohit','ajay']
    }


#dynamic routes or path paramerers
@app.get("/user/{user_id}")
def user(user_id:int):
    return {"userid" : user_id}

#query parameter

@app.get("/user")  #this was a good one
def user(id: int=None):  #here none is default value
    return{
        "name": id
    }

#query parameter 

@app.get("/amozon")
def amozon(laptop: str=None,price : int=None):
    return {
        "laptopname":laptop,
        "laptopprice": price


    }

#//////////////////////////////////////////
           #practice
#////////////////////////////////////////////


BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008, "available": True},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2022, "available": True},
    {"id": 3, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999, "available": False},
    {"id": 4, "title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017, "available": True},
    {"id": 5, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019, "available": False},
]


@app.get("/books")
def books():
  return BOOKS



#//////////////////////////////////////////
           #practice
#////////////////////////////////////////////




from pydantic import BaseModel,EmailStr
class User(BaseModel):
    name:str
    age: int

@app.post("/create_user")
def create_user(user:User):
    return {
        "data": user
    }

###################################
####################################

class Address(BaseModel):
    H_NO:int
    pincode:int
    landmark:str

class information(BaseModel):
    name:str
    age:int
    id:int
    address:Address

@app.post("/user_information")
def user_information(data:information):
    return {
        "this is user data":data
        
    }

#############################################
################################################
################################################
         #curd operation#

class Todo(BaseModel):
    id:int
    task:str
    flag:bool

todos: list[Todo] = []
 
#now i am creating a postapi where i will insert data insid todoslist ok

@app.post("/user_data")
def todo(temp:Todo):
    todos.append(temp)
    return{
        "inset data inside this basemodel":temp
    }

print(todos)

@app.get("/todaytodo")
def usertodaytodo():
    return todos


#geting single data

@app.get("/todo/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo

    return {"roor todo not found"}   


#upadate operation 

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]==updated_todo
            return{
                "message":"Data updated",
                "data":updated_todo
            }
    return {"error":"Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_tot(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return {"messeage":"data Deleted"}
    return {"error ":"Todo not found"}



