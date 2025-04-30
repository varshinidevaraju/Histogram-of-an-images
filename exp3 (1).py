#!/usr/bin/env python
# coding: utf-8

# In[44]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[45]:


## Histogram Equalization for Grayscale Images


# In[46]:


# Read the image in grayscale format.
img = cv2.imread('parrot.jpg', cv2.IMREAD_GRAYSCALE)


# In[47]:


# Display the images.
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.show()


# In[48]:


# Display the images
plt.hist(img.ravel(),256,range = [0, 256]);
plt.title('Original Image')
plt.show()


# In[49]:


# Equalize histogram
img_eq = cv2.equalizeHist(img)


# In[50]:


# Display the images.
plt.hist(img_eq.ravel(), 256, range = [0, 256]); 
plt.title('Equalized Histogram')


# In[51]:


# Display the images.
plt.imshow(img_eq)
plt.title('Equilization Image')
plt.show()


# In[52]:


##Histogram Equalization for Color Images


# In[29]:


# Read the color image.
img = cv2.imread('parrot.jpg', cv2.IMREAD_COLOR)


# In[30]:


# Convert to HSV.
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# In[31]:


# Perform histogram equalization only on the V channel, for value intensity.
img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:, :, 2])


# In[32]:


# Convert back to BGR format.
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)


# In[33]:


# Display the images.
plt.subplot(121); plt.imshow(img[:, :, ::-1]); plt.title('Original Color Image')
plt.subplot(122); plt.imshow(img_eq[:, :, ::-1]); plt.title('Equalized Image')


# In[34]:


# Display the histograms.
plt.figure(figsize = [15,4])
plt.subplot(121); plt.hist(img.ravel(),256,range = [0, 256]); plt.title('Original Image')
plt.subplot(122); plt.hist(img_eq.ravel(),256,range = [0, 256]); plt.title('Histogram Equalized')


# In[ ]:





# In[ ]:




