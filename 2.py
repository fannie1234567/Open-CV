#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from google.colab.patches import cv2_imshow

a = cv2.imread('h2.png')
cv2_imshow(a)


# In[ ]:


b = np.full(a.shape,(0,0,255),np.uint8)
cv2_imshow(b)


# In[ ]:


c = cv2.absdiff(a,b)
cv2_imshow(c)


# In[ ]:


d = cv2.add(cv2.add(c[:,:,0],c[:,:,1]),c[:,:,2])
cv2_imshow(d) 


# In[ ]:


d.shape


# In[ ]:


e = cv2.multiply(d,b[:,:,2])
cv2_imshow(e)


# In[ ]:


e.shape


# In[ ]:


f = np.full(a.shape,(255,255,255),np.uint8)
f[:,:,0] = e
f[:,:,1] = e
f[:,:,2] = e
cv2_imshow(f)


# In[ ]:


e.shape


# In[ ]:




