# Histogram-of-an-images
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the gray and color image using imread()

### Step2:
Print the image using imshow().

### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.


## Program:
```python
# Developed By: DEVADHAARINI.D
# Register Number: 212223230040

import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread('img0.jpg')
color_image = cv2.imread('img1.jpg')
cv2.imshow("Gray image",gray_image)
cv2.imshow("color image",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()      


import numpy as np
gray_image=cv2.imread('img0.jpg')
import matplotlib.pyplot as plt 
gray_hist=cv2.calcHist(gray_image,[0],None,[255],[0,255])
plt.figure()
plt.imshow(gray_image)
plt.show()
plt.title("Histogram")
plt.xlabel("Grayscale value")
plt.ylabel("pixel count")
plt.stem(gray_hist)
plt.show()


import numpy as np
color_image=cv2.imread('img1.jpg')
import matplotlib.pyplot as plt 
color_hist=cv2.calcHist(color_image,[0],None,[255],[0,255])
plt.figure()
plt.imshow(color_image)
plt.show()
plt.title("Histogram")
plt.xlabel("Colorscale value")
plt.ylabel("pixel count")
plt.stem(color_hist)
plt.show()


import cv2
gray_image = cv2.imread("img0.jpg",0)
cv2.imshow('Grey Scale Image',gray_image)
equ = cv2.equalizeHist(gray_image)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
## Output:
### Input Grayscale Image and Color Image
![WhatsApp Image 2025-04-08 at 08 33 05_a493c878](https://github.com/user-attachments/assets/ba41ab6f-7cb5-453c-b644-76a610218b73)
![WhatsApp Image 2025-04-08 at 08 33 05_2600bdbb](https://github.com/user-attachments/assets/1079f658-3d90-4ae6-a6f9-970c8720fbcb)

### Histogram of Grayscale Image and any channel of Color Image
![image](https://github.com/user-attachments/assets/fd2e6fa0-d141-4606-9733-9863b91eb2d9)
![image](https://github.com/user-attachments/assets/f7fcecd7-6071-4006-ac65-90b445c2ffe2)

### Histogram Equalization of Grayscale Image.
![image](https://github.com/user-attachments/assets/b5c3ccf9-6026-4852-bc0d-2a13d632e30f)

## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
