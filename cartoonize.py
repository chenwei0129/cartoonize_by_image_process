import cv2
import numpy as np

original_image = cv2.imread('0.jpg')

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

median_filtered_image = cv2.medianBlur(gray_image, 5)

edges = cv2.Canny(median_filtered_image, 60, 120)

kernel = np.ones((2, 2), np.uint8)

dilated_image = cv2.dilate(edges, kernel, iterations=1)
#dilated_image = edges
dilated_image_3D = np.dstack((dilated_image, dilated_image, dilated_image))

blue_channel, green_channel, red_channel = cv2.split(original_image)

blue_smoothed_image_Q = cv2.blur(blue_channel, (3, 3))
green_smoothed_image_Q = cv2.blur(green_channel, (3, 3))
red_smoothed_image_Q = cv2.blur(red_channel, (3, 3))

mask1 = (blue_smoothed_image_Q >= 0) & (blue_smoothed_image_Q <= 31)
blue_smoothed_image_Q[mask1] = 0
mask2 = (blue_smoothed_image_Q >= 32) & (blue_smoothed_image_Q <= 63)
blue_smoothed_image_Q[mask2] = 47
mask3 = (blue_smoothed_image_Q >= 64) & (blue_smoothed_image_Q <= 95)
blue_smoothed_image_Q[mask3] = 80
mask4 = (blue_smoothed_image_Q >= 96) & (blue_smoothed_image_Q <= 127)
blue_smoothed_image_Q[mask4] = 112
mask5 = (blue_smoothed_image_Q >= 128) & (blue_smoothed_image_Q <= 159)
blue_smoothed_image_Q[mask5] = 144
mask6 = (blue_smoothed_image_Q >= 160) & (blue_smoothed_image_Q <= 191)
blue_smoothed_image_Q[mask6] = 176
mask6 = (blue_smoothed_image_Q >= 192) & (blue_smoothed_image_Q <= 223)
blue_smoothed_image_Q[mask6] = 208
mask6 = (blue_smoothed_image_Q >= 224) & (blue_smoothed_image_Q <= 255)
blue_smoothed_image_Q[mask6] = 255

mask1 = (green_smoothed_image_Q >= 0) & (green_smoothed_image_Q <= 31)
green_smoothed_image_Q[mask1] = 0
mask2 = (green_smoothed_image_Q >= 32) & (green_smoothed_image_Q <= 63)
green_smoothed_image_Q[mask2] = 47
mask3 = (green_smoothed_image_Q >= 64) & (green_smoothed_image_Q <= 95)
green_smoothed_image_Q[mask3] = 80
mask4 = (green_smoothed_image_Q >= 96) & (green_smoothed_image_Q <= 127)
green_smoothed_image_Q[mask4] = 112
mask5 = (green_smoothed_image_Q >= 128) & (green_smoothed_image_Q <= 159)
green_smoothed_image_Q[mask5] = 144
mask6 = (green_smoothed_image_Q >= 160) & (green_smoothed_image_Q <= 191)
green_smoothed_image_Q[mask6] = 176
mask6 = (green_smoothed_image_Q >= 192) & (green_smoothed_image_Q <= 223)
green_smoothed_image_Q[mask6] = 208
mask6 = (green_smoothed_image_Q >= 224) & (green_smoothed_image_Q <= 255)
green_smoothed_image_Q[mask6] = 255

mask1 = (red_smoothed_image_Q >= 0) & (red_smoothed_image_Q <= 31)
red_smoothed_image_Q[mask1] = 0
mask2 = (red_smoothed_image_Q >= 32) & (red_smoothed_image_Q <= 63)
red_smoothed_image_Q[mask2] = 47
mask3 = (red_smoothed_image_Q >= 64) & (red_smoothed_image_Q <= 95)
red_smoothed_image_Q[mask3] = 80
mask4 = (red_smoothed_image_Q >= 96) & (red_smoothed_image_Q <= 127)
red_smoothed_image_Q[mask4] = 112
mask5 = (red_smoothed_image_Q >= 128) & (red_smoothed_image_Q <= 159)
red_smoothed_image_Q[mask5] = 144
mask6 = (red_smoothed_image_Q >= 160) & (red_smoothed_image_Q <= 191)
red_smoothed_image_Q[mask6] = 176
mask6 = (red_smoothed_image_Q >= 192) & (red_smoothed_image_Q <= 223)
red_smoothed_image_Q[mask6] = 208
mask6 = (red_smoothed_image_Q >= 224) & (red_smoothed_image_Q <= 255)
red_smoothed_image_Q[mask6] = 255

color_image_Q = np.dstack((blue_smoothed_image_Q, green_smoothed_image_Q, red_smoothed_image_Q))

mask = dilated_image_3D == 255
color_image_Q[mask] = 0

merged_image = np.hstack((original_image, color_image_Q))

cv2.imshow('original and cartoon image', merged_image)
cv2.waitKey(0)
