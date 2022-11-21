from fastapi import FastAPI
from pydantic import BaseModel
from transcribe import trans
app = FastAPI()

class Address(BaseModel):
    resource_link: str

@app.get("/")
async def root():
    print("wait")
    return {"message": "Welcome Processor, its a good day."}




@app.post("/transpile/")
async def transpile(address: Address):
    print(address.resource_link)
    data = trans(address.resource_link)
    return data