

from zipfile import ZipFile
import pickle
import sklearn

with ZipFile('model.zip', 'r') as zip:
  data = zip.read('model.pkl')

model=pickle.loads(data)
preditions=model.predict([[1,24,200,80,199,43,2012,3,19,9,160]])
print(preditions)