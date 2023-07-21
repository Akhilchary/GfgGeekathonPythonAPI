

from zipfile import ZipFile
import pickle
from fastapi import FastAPI
import sklearn
from pydantic import BaseModel

app=FastAPI()



with ZipFile('model.zip', 'r') as zip:
  data = zip.read('model.pkl')

model=pickle.loads(data)
preditions=model.predict([[1,24,200,80,199,43,2012,3,19,9,160]])
print(preditions)

class Mock(BaseModel):
  name:str
  prof:str


# API
@app.get('/')
async def root():
  return {"message":"hello"}

# demonstration of get request
@app.get('/printname/{name}')
async def printName(name):
  return {"lolname":name}

# post request
@app.post('/post')
async def funcname(obj:Mock):
  print(obj.name+obj.prof)
  # print(obj)
  return obj