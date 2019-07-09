
# coding: utf-8

# In[3]:


import cv2


# In[4]:


x=cv2.VideoCapture(0)


# In[ ]:


ret,pic=x.read()
ret1,pic1=x.read()


# In[5]:


pic = cv2.imread("pic.png")
pic1=cv2.imread("pic1.png")


# In[ ]:


cv2.imwrite("pic.png",pic)
cv2.imwrite("pic1.png",pic1)


# In[9]:


pic1[0:100,0:100]=pic[200:300,300:400]


# In[10]:


cv2.imshow("hi",pic1)
cv2.waitKey()
cv2.destroyAllWindows()

