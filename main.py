from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def home():
    return {"message":"hello,vro"}

@app.get("/user/{name}")
def user(name):
    return{"message":f"hello {name}"}

@app.get("/user/Sai")
def uo():
    return{"message":"hello sai"}
class Student(BaseModel):
    name:str
    age:int
    marks:float
@app.post("/student")
def student(data:Student):
    return data
class PredictionData(BaseModel):
    age:int
    income:int
    balance:float|None=None
# @app.post("/predict")
# def predict(data:PredictionData):
#     return{
#         "age":data.age,
#         "income":data.income,
#         "balance":data.balance,
#         "message":"Data received successfully"
#     }
class PredictResponse(BaseModel):
    message:str
    prediction:int
@app.post("/predict",response_model=PredictResponse)
def predict(data:PredictionData):
    return{
        "message":"prediction completed",
        "prediction":680
    }
