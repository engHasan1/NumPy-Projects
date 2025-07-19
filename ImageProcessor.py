import numpy as np
import matplotlib.pyplot as plt 


#Generating a random image array and displaying it using matplotlib
image=np.random.randint(0,256,size=(10,10))

# Inverting the image array
inverted_image = 255 - image

# Brightening the image by adding a constant value
brighter_image = np.clip(image + 100, 0, 255)



# Darkening the image by subtracting a constant value
darker_image = np.clip(image - 50, 0, 255)

#resizing the image to 10x10
resiz_image = np.resize(image, (5, 5))


# Cropping the image by setting the first 7 rows to zero
cropped_image = np.copy(image)
cropped_image[7:, :] = 0

#displaying all images
plt.figure(figsize=(10, 10))
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title('Original Image')
plt.subplot(2, 3, 2)
plt.imshow(inverted_image, cmap='gray', vmin=0, vmax=255)
plt.title('Inverted Image')
plt.subplot(2, 3, 3)
plt.imshow(brighter_image, cmap='gray', vmin=0, vmax=255)
plt.title('Brighter Image')
plt.subplot(2, 3, 4)
plt.imshow(darker_image, cmap='gray', vmin=0, vmax=255)
plt.title('Darker Image')
plt.subplot(2, 3, 5)
plt.imshow(cropped_image, cmap='gray', vmin=0, vmax=255)
plt.title('Cropped Image')
plt.subplot(2, 3, 6)
plt.imshow(resiz_image, cmap='gray', vmin=0, vmax=255)
plt.title('Resized Image(5x5)')


plt.show()