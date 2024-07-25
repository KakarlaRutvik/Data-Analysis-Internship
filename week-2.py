#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
cars = pd.read_csv('Data-ware House Mining/mycar.csv')
print(cars)


# In[3]:


type(cars)


# In[4]:


cars.info


# In[5]:


cars.describe()


# In[6]:


cars.isnull()


# In[7]:


import numpy as np
from scipy import stats


# In[9]:


cars.columns


# In[10]:


cars.drop(['Unnamed: 0'], axis=1, inplace=True)


# In[11]:


cars


# In[12]:


cars.columns


# In[ ]:




