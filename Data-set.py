#!/usr/bin/env python
# coding: utf-8

# In[8]:

# Data Analysis with Python Week - 1 Task
# Data structures in python 
my_set = {10, 20, 30, 40, 50}
print("Set:", my_set)


# In[9]:


my_set.add(60)
print("Set after adding:", my_set)


# In[10]:


my_set.remove(30)
print("Set after removing:", my_set)


# In[11]:


another_set = {40, 50, 60, 70, 80}


# In[12]:


union_set = my_set.union(another_set)
print("Union of my_set and another_set:", union_set)


# In[13]:


intersection_set = my_set.intersection(another_set)
print("Intersection of my_set and another_set:", intersection_set)


# In[14]:


difference_set = my_set.difference(another_set)
print("Difference between my_set and another_set:", difference_set)


# In[ ]:




