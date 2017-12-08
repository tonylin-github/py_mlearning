#import sys
#print(sys.platform)
import os
import pandas as pd
import requests

PATH=r'/home/admin/python_base/'
r=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
with open(PATH+'iris.data','w') as f:
    f.write(r.text)

os.chdir(PATH)
cur_dir=os.getcwd()
#print("cur_dir=%s"%(cur_dir))
df=pd.read_csv('/home/admin/python_base/iris.data',names=['sepal length','sepal width','petal length','petal width','class'])
#df.head()
#print (df.head().to_csv(columns=['sepal length','sepal width','petal length','petal width','class'],sep='\t',index=True))

#print (df['sepal length'])

#print (df.ix[:3,:2])
#print (df.ix[:3,[x for x in df.columns if 'width' in x]])
#print (df['class'].unique())

print (df[df['class]=='Iris-setosa'])


