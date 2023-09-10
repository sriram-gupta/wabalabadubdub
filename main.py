from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def HealthCheck():
    return "<h1>Welcome Home ! (C) SRK </h1>"


@app.get("/health")
def HealthCheck():
    return { "status": "ok", "msg": "Health Check Working Properly" }

