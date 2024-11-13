#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.read_csv("diabetes.csv")


# In[5]:


df.head()


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[9]:


X=df.iloc[:,:-1].to_numpy()


# In[10]:


y=df.iloc[:,-1].to_numpy()


# In[15]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


# In[17]:


from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(criterion="entropy",random_state=0)
clf.fit(X_train,y_train)


# In[19]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.tree import plot_tree
clf.fit(X_train,y_train)
plt.figure(figsize=(10,20))
plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()


# In[20]:


clf.set_params(max_depth=3)


# In[22]:


clf.fit(X_train,y_train)
plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()


# In[23]:


predictions=clf.predict(X_test)


# In[24]:


clf.predict([[90,20],[200,30]])


# In[25]:


predictions


# In[ ]:




