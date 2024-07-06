# Data Analysis with Python Week - 1 Task
# Data structures in python 
#!/usr/bin/env python
# coding: utf-8

# In[13]:


my_dict = {
    "name": "Mahendra Singh Dhoni",
    "age": 42,
    "city": "Ranchi",
    "international cups":(2007,2011),
    "ipl cups":5
}
print("Dictionary:", my_dict,"\n")


# In[14]:


my_dict["nickname"] = "Thala"
print("Ms Dhoni:", my_dict)


# In[15]:


name = my_dict["name"]
print("Name:", name)


# In[16]:


my_dict["city"] = "Ranchi, India"
print("Dictionary after updating city:", my_dict)

