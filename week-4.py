#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
data = pd.read_csv('c.csv')
data


# In[10]:


print(data.info())


# In[11]:


print(data.isnull().sum())


# In[12]:


print(data.isnull().sum())
data = data.dropna()


# In[17]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sns.histplot(data['Rating'], kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['Rating'])
plt.title('Box Plot of Ratings')
plt.xlabel('Rating')
plt.show()
data['comment_length'] = data['Comment'].apply(len)
plt.figure(figsize=(10, 6))
sns.histplot(data['comment_length'], kde=True)
plt.title('Distribution of Comment Lengths')
plt.xlabel('Comment Length')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['comment_length'])
plt.title('Box Plot of Comment Lengths')
plt.xlabel('Comment Length')
plt.show()


# In[18]:


correlation_matrix = data[['Rating', 'comment_length']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()


# In[19]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Rating', y='comment_length', data=data)
plt.title('Scatter Plot of Rating vs. Comment Length')
plt.xlabel('Rating')
plt.ylabel('Comment Length')
plt.show()


# In[ ]:




