#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('p.csv')
data


# In[3]:


print("\nData types of the columns:")
print(data.dtypes)


# In[4]:


data['Purchased'] = data['Purchased'].map({'Yes': 1, 'No': 0})


# In[6]:


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(data['Age'], kde=True)
plt.title('Distribution of Age')

plt.subplot(1, 2, 2)
sns.histplot(data['Salary'], kde=True)
plt.title('Distribution of Salary')
plt.show()


# In[7]:


plt.figure(figsize=(6, 4))
sns.countplot(x='Purchased', data=data)
plt.title('Count of Purchased')
plt.xlabel('Purchased')
plt.ylabel('Count')
plt.show()


# In[8]:


sns.pairplot(data, hue='Purchased', vars=['Age', 'Salary'])
plt.show()


# In[9]:


plt.figure(figsize=(8, 6))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[ ]:




