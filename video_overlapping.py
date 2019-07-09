
# coding: utf-8

# In[24]:


import cv2


# In[25]:


cap=cv2.VideoCapture(0)


# In[28]:


while True:
    ret,pic=cap.read()
    new=pic[100:300,300:500]   
    pic[:200,:200]=new
    cv2.imshow('hi',pic)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()


# In[29]:


cap.release()

