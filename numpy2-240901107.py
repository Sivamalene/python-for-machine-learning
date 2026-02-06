#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
print("Original array:\n",arr)


# In[2]:


import numpy as np
arr=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
temp=arr[[0,1,2,3],[3,2,1,0]]
print("\nElements at indices(0,3),(1,2),(2,1),""(3,0):\n",temp)


# In[3]:


import numpy as np
arr=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
cond=arr>2
temp=arr[cond]
print("\nElements greater than 2:\n",temp)


# In[6]:


import numpy as np
arr=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print("\nOriginal arrays:\n",arr1,arr2)
print("\nJoined array:\n",arr)


# In[7]:


arr=np.hstack((arr1,arr2))
print("\nHorizontal joining:\n",arr)


# In[8]:


arr=np.vstack((arr1,arr2))
print("\nVertical joining:\n",arr)


# In[9]:


arr=np.dstack((arr1,arr2))
print("\nDepth joining:\n",arr)


# In[12]:


arr=np.array([1,2,3,4,5,6]) 
newarr=np.array_split(arr,3)
print("\nOriginal Array:\n",arr)
print("\nSplitted array:\n",newarr)
print("\nSplitted array in another form:\n")
print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[13]:


print("\nEvery other rows:\n",arr[0:3:2])


# In[16]:


arr=np.array([1,2,3,4,5,6,7])
print("\nOriginal array:",arr)
print("\nReturn every other elements in the array:arr[::2]:",arr[::2])


# In[17]:


import numpy as np
arr=np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
temp=arr[:2,:3]
print("\nArray with first 2 rows and 3 column:\n",temp)


# 
