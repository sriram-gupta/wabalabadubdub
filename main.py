from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pickle
from mlUtils import HeightPredictor

app = FastAPI()


@app.get("/",response_class=HTMLResponse)
def HealthCheck():
    return "<h1>Welcome Home ! (C) SRK </h1>"


@app.get("/health")
def HealthCheck():
    return { "status": "ok", "msg": "Health Check Working Properly" }

@app.get("/ml/{weight}")
def MachineLearningModel(weight: float):
    if(type(weight) != int and type(weight) != float):
        return "not int or float"
    else:
        return HeightPredictor(weight)