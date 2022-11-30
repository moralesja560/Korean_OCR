import matplotlib.pyplot as plt

import cv2



# Converting image to grayscale color space
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# Applying thresholds and storing the returned values in two variables
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# Plotting the images using matplotlib
titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
thresholding = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# Specifying the grid size
plt.figure(figsize=(10,10))
# The number of images in the grid 2*3 = 6
for i in range(6):
plt.subplot(2,3,i+1),plt.imshow(thresholding[i],'gray',vmin=0,vmax=255)
plt.title(titles[i])
    
# Displaying the grid    
plt.show()