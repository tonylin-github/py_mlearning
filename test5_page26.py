import os
import pandas as pd
import requests
import matplotlib.pyplot as plt
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
fig,ax=plt.subplots(figsize=(7,7))

ax.scatter(df['sepal width'][:50],df['sepal length'][:50])
ax.set_ylabel('sepal length')
ax.set_xlabel('sepal width')
ax.set_title('setosa sepa width vs sepal length',fontsize=14,y=1.02)

#print(df.groupby('class')['petal width'].agg({'delta':lambda x:x.max()-x.min(),'max':np.max,'min':np.min}))

'''
ax[0][0].hist(df['petal width'],color='black')
ax[0][0].set_ylabel('count',fontsize=12)
ax[0][0].set_xlabel('width',fontsize=12)
ax[0][0].set_title('Iris Petal Width',fontsize=14,y=1.01)


ax[0][1].hist(df['petal length'],color='black')
ax[0][1].set_ylabel('count',fontsize=12)
ax[0][1].set_xlabel('width',fontsize=12)
ax[0][1].set_title('Iris Petal length',fontsize=14,y=1.01)


ax[1][0].hist(df['sepal width'],color='black')
ax[1][0].set_ylabel('count',fontsize=12)
ax[1][0].set_xlabel('width',fontsize=12)
ax[1][0].set_title('Iris sepal Width',fontsize=14,y=1.01)

ax[1][1].hist(df['sepal length'],color='black')
ax[1][1].set_ylabel('count',fontsize=12)
ax[1][1].set_xlabel('width',fontsize=12)
ax[1][1].set_title('Iris sepal length',fontsize=14,y=1.01)
'''
#fig.savefig("20171211v2.png")
