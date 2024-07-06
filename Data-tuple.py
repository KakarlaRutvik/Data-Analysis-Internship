#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_tuple=(7,18,33,45,93)
print(my_tuple)


# In[5]:


no_1 = my_tuple[1]
print("The value at index 1 is:", no_1)


# In[11]:


new_value = int(input("enter a value to add"))
my_tuple = my_tuple + (new_value,)
print(my_tuple)


# In[12]:


my_list_tuple=list(my_tuple)
print(my_list_tuple)


# In[14]:


delete_value=int(input("enter a value to delete"))
if delete_value in my_list_tuple:
    my_list_tuple.remove(delete_value)
    print(f"Value {delete_value} deleted from the list")
    my_tuple = tuple(my_list_tuple)
    print("Tuple after deleting the value:", new_tuple)
else:
    print(f"Value {delete_value} not found in the tuple")


# In[16]:


old_value = int(input("enter value to be updated"))
new_value = int(input("enter value to update"))
if old_value in my_list_tuple:
    index = my_list_tuple.index(old_value)
    my_list_tuple[index] = new_value
    my_tuple = tuple(my_list_tuple)
    print(f"List after updating {old_value} to {new_value}:", my_tuple)
else:
    print(f"{old_value} is not in the list.")

