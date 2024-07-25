#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
house = pd.read_csv('Machine Learning/Delhi_v2.csv')
house


# In[2]:


house.head()


# In[3]:


plt.figure(figsize=(10, 6))
plt.bar(house['area'], house['price'], color='blue')
plt.title('Area wise Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()


# In[4]:


plt.figure(figsize=(10, 6))
plt.plot(house['area'], house['price'], marker='o', linestyle='-', color='blue', label='Price vs Area')
plt.title('Area vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()


# In[ ]:




