#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd


# In[17]:


d={'Country':['France','Spain','Germany','Spain','Germany','France','Spain','France','Germany','France'], 
   'Age':[44,27,30,38,40,35,np.nan,48,50,37],
   'Salary':[72000,48000,54000,61000,np.nan,58000,52000,79000,83000,67000],
   'Purchased':['No','Yes','No','No','Yes','Yes','No','Yes','No','Yes']}
d


# In[18]:


df1=pd.DataFrame(d)


# In[15]:


df1


# In[ ]:


df1 = pd.DataFrame(d)


# In[16]:


df1


# In[20]:


df1 = pd.DataFrame(d)


# In[21]:


df1


# In[22]:


df1['Age'].mean()


# In[23]:


df1


# In[24]:


df1['Age'] = df1['Age'].fillna(df1['Age'].mean())


# In[25]:


df1


# In[26]:


df1['Salary'].mean()


# In[27]:


df1


# In[28]:


df1['Salary'] = df1['Salary'].fillna(df1['Salary'].mean())


# In[29]:


df1


# In[30]:


df1 = df1.drop_duplicates()


# In[31]:


df1


# In[32]:


df1 = df1.drop(1)


# In[33]:


df1


# In[34]:


df1.loc[10]=['Spain',35,35000,'Yes']


# In[35]:


df1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




