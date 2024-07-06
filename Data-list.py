#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Data Analysis with Python Week - 1 Task
# Data structures in python 

# List
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)


# In[3]:


user_input = int(input("Enter a value to add in list: "))
my_list.append(user_input)
print("List after appending the user input value:", my_list)


# In[4]:


value_to_check = int(input("Enter a value to check if it is in the list: "))
if value_to_check in my_list:
    print(f"{value_to_check} is in the list.")
else:
    print(f"{value_to_check} is not in the list.")


# In[5]:


old_value = int(input("Enter the value to be updated: "))
new_value = int(input("Enter the new value: "))

if old_value in my_list:
    index = my_list.index(old_value)
    my_list[index] = new_value
    print(f"{old_value} has been updated to {new_value} in the list. Now the list is {my_list}")
else:
    print(f"{old_value} is not in the list.")


# In[6]:


value_to_remove = int(input("Enter a value to remove from the list: "))
if value_to_remove in my_list:
    my_list.remove(value_to_remove)
    print(f"{value_to_remove} has been removed from the list. Now the list is {my_list}")
else:
    print(f"{value_to_remove} is not in the list.")


# In[ ]:




