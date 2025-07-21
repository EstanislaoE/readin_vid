import cv2
import numpy as np 

"""
Add gray scale dim (x, x, 1)
"""

# image_read = cv2.imread("tiger.jpg", cv2.IMREAD_GRAYSCALE)
# #cv2.imwrite("tiger_gray.jpg", image_read)
# #print(image_read)
# print(image_read.shape)
# print("")
# gray_scale_image_channel = np.expand_dims(image_read, axis = 2)
# print("Adding gray scale dimension 1")
# print(gray_scale_image_channel.shape)

"""
compress image
"""
# image_read = cv2.imread("tiger.jpg", cv2.IMREAD_COLOR)
# print(image_read.shape)
# print("")
# cv2.imwrite("compression_im.png", image_read, [cv2.IMWRITE_PNG_COMPRESSION, 7])

"""
Splitting images to BGR
"""
# image_read = cv2.imread("tiger.jpg", cv2.IMREAD_COLOR)
# print("Pixel data:\n")
# #print(image_read)
# b, g, r = cv2.split(image_read)
# cv2.imwrite("b_image.jpg", b)
# cv2.imwrite("g_image.jpg", g)
# cv2.imwrite("r_image.jpg", r)

# #MERGE them together 
# cv2.imwrite("merged_bgr_image.jpg", cv2.merge((r, b, g)))



"""
Specify Image Size 
"""
# image_read = cv2.imread("tiger.jpg", cv2.IMREAD_COLOR)
# print("Original image size:")
# print(image_read.shape)

# resized_image = cv2.resize(image_read, (2800, 2200))
# cv2.imwrite("tiger_small.jpg", resized_image)
# print(resized_image.shape)


"""
BGR to RGB
"""
# image_read = cv2.imread("tiger.jpg", cv2.IMREAD_COLOR)
# print("Original image size:")
# print(image_read.shape)

# rgb_image = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
# cv2.imwrite("rgb_image.jpg", rgb_image)

"""
HSV 
"""
image_read = cv2.imread("tiger.jpg", cv2.IMREAD_COLOR)
print("Original image size:")
print(image_read.shape)

hsv_image = cv2.cvtColor(image_read, cv2.COLOR_BGR2HSV)
cv2.imwrite("HSV_image.jpg", hsv_image)