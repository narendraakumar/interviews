#!/usr/bin/env python
# coding: utf-8

# Write a function to reverse odd or even rows in matrix.
# Mat = [[ 1,2,3,4],
# [5,6,7,8],
# [9,10,11,12]]
# reverse_matrix(mat,row=”odd”) -> 
# [[ 1,2,3,4],
# [8,7,6,5],
# [9,10,11,12]]
# reverse_matrix(mat,row=”even”)->
# [[ 4,3,2,1],
# [5,6,7,8],
# [12,11,10,9]]
# 
# 

# In[1]:


mat = [[ 1,2,3,4], [5,6,7,8], [9,10,11,12]] 


# In[5]:


mat = [[ 1,2,3,4], [5,6,7,8],[1,2,2,2], [9,10,11,12]] 


# In[12]:


def catch_index(mat):

    len_mat = len(mat)

    even_temp = []

    odd_temp = []

    for i in range(len_mat):

        if i%2 == 0:

            even_temp.append(i)

        else:

            odd_temp.append(i)
    
    return even_temp, odd_temp


# In[10]:


mat = [[ 1,2,3,4], [5,6,7,8], [9,10,11,12]] 


# In[15]:




def reverse_custom(mat,row):
    
    if row == "odd":
        
        even_temp, odd_temp = catch_index(mat)
        
        for ele in odd_temp:
            
            val = mat[ele] 
            
            mat[ele] = val[::-1]
    
    if row == "even":
        
        even_temp, odd_temp = catch_index(mat)
        
        for ele in even_temp:
            
            val = mat[ele] 
            
            mat[ele] = val[::-1]
    
    return mat
              


# In[17]:


reverse_custom(mat,"odd")


# In[18]:


reverse_custom(mat,"even")


# Given a string of size n, write functions to perform following operations on string.
# Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
# Right (Or clockwise) rotate the given string by d elements (where d <= n).
# Examples:
# 
# Input : s = "whatismyname"
#         d = 2
# Output : Left Rotation  : "atismynamewh" 
#          Right Rotation : "mewhatismyna"  
# Input : s = "qwertyu" 
#         d = 2
# Output : Left rotation : "ertyuqw"
#          Right rotation : "yuqwert

# In[30]:


def string_man(string, d_len, clock_type):
    
    if clock_type == "Left Rotation":
    
        str1 = string
        
        str2 = str1[d_len:]
        
        str3 = str1[:d_len]
        
        modified_str =   str2 + str3
        
    return modified_str


# In[31]:


string_man("whatismyname", 2, "Left Rotation")


# In[21]:


a = "whatismyname"


# In[25]:


b = a[2:]


# In[26]:


c = a[:2]


# In[27]:


b + c


# Write a function to generate a matrix of size n,m. The centermost elements should be 1, as me move towards the outer elements, the value should increment by 1. For example.
# For a 3x3 matrix
# [[2,2,2],
# [2,1,2],
# [2,2,2],]
# For 4x4 Matrix
# [[2, 2, 2, 2],
# [2, 1, 1, 2],
# [2, 1, 1, 2],
# [2, 2, 2, 2],]
# For 5x5 Matrix(
# [[3, 3, 3, 3 ,3]
# [3, 2, 2, 2, 3]
# [3, 2, 1, 2, 3]
# [3, 2, 2, 2 ,3]
# [3, 3, 3, 3 ,3] ]

# In[38]:


import numpy as np

s = (5,5)

x = np.ones(s) 


# In[ ]:





# In[ ]:





# In[ ]:




