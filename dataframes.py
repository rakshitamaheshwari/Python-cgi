
# coding: utf-8

# In[2]:


import pandas as pd


# In[11]:


myname=[["vimal",111],["krish",222],["pop",333]]


# In[15]:


d=pd.DataFrame(data=myname,columns=["Name","Contact"])


# In[16]:


d


# In[20]:


d['Name']


# In[22]:


d.iloc[0]


# In[23]:


d.loc[0]


# In[31]:


m={"a":["vimal",1],"b":["abc",22]}


# In[32]:


m=pd.DataFrame(m)


# In[33]:


m


# In[34]:


m.loc[0:2]


# In[35]:


m.iloc[1]

