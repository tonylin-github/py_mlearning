import os
import pandas as pd
import requests
import matplotlib.pyplot as plt
import statsmodels.api as sm

plt.style.use('ggplot')
%matplotlib inline
import numpy as np

PATH=r'/home/admin/python_base/'
#r=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/\
#iris.data')
#with open(PATH+'iris.data','w') as f:
#    f.write(r.text)

#os.chdir(PATH)
#cur_dir=os.getcwd()
#print("cur_dir=%s"%(cur_dir))                                                  
df=pd.read_csv('/home/admin/python_base/iris.data',names=['sepal length','sepal\
 width','petal length','petal width','class'])
#print(df.corr(method="kendall"))
y=df['sepal length'][:50]
x=df['sepal width'][:50]
X=sm.add_constant(x)
results=sm.OLS(y,X).fit()
print(results.summary())

