
# https://www.kaggle.com/code/rahul1394/weight-height-prediction-linear-regression

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import r2_score,mean_squared_error



import pickle

# Load the data 
weight_height_dataset = pd.read_csv('./weight-height.csv')
print(weight_height_dataset.head())


from sklearn.model_selection import train_test_split

x = pd.DataFrame(weight_height_dataset['Weight'])
y = pd.DataFrame(weight_height_dataset['Height'])


xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.30,random_state=31)
print(xtrain.shape,ytrain.shape,xtest.shape,ytest.shape)



from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(xtrain,ytrain)
yPredict = lr.predict(xtest)
print(yPredict)

accuracy = r2_score(ytest,yPredict)
print(" Accuracy : {}".format(accuracy))

filename = "height_prediction_model"
pickle.dump(lr, open(filename,'wb'))

print(lr.predict([[241]])) # input weight and get height 