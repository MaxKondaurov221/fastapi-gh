from fastapi import FastAPI, Depends
import uvicorn
from views.calc import router as router_calc
app = FastAPI()
app.include_router(router_calc, prefix="/calc")
@app.get("/hello")
def hello_by_qs(name:str = "World"):
    return {"message": f"Hello! {name}"}

@app.get("/hello/{name}")
def hello_by_path(name:str):
    return {"message": f"Hello {name}"}


@app.get("/hi")
@app.get("/hi/{name}")
def hello_by_path(name:str = 'World'):
    return {"message": f"Hi {name}"}
@app.post("/hello/{name}")
def hello_by_path(name:str = 'World'):
    return {"message": f"Hello {name}"}




if __name__ == '__main__':
    uvicorn.run(app)
