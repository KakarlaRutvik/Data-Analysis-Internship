#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data=pd.read_csv("Iris.csv")
data.head()


# In[3]:


from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
data['species']=label_encoder.fit_transform(data['species'])
data


# In[4]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
data=sc.fit_transform(data)
data=pd.DataFrame(data)
data


# In[5]:


from sklearn.decomposition import PCA
pca=PCA(n_components=2)
df_final=pca.fit_transform(data)
df_final=pd.DataFrame(df_final)
df_final


# In[6]:


df_final.columns=['A','B']
print("The principal comoponents of the data are")
df_final


# In[7]:


import matplotlib.pyplot as plt 
plt.scatter(df_final['A'],df_final['B'],color=('red'))


# In[ ]:




