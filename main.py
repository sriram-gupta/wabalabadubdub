from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def HealthCheck():
    return "<h1>Welcome Home ! (C) SRK </h1>"


@app.get("/health")
def HealthCheck():
    return { "status": "ok", "msg": "Health Check Working Properly" }

