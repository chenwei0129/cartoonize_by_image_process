import cv2
import numpy as np

original_image = cv2.imread('test2.png')

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

median_filtered_image = cv2.medianBlur(gray_image, 5)

edges = cv2.Canny(median_filtered_image, 50, 100)

kernel = np.ones((2, 2), np.uint8)

dilated_image = cv2.dilate(edges, kernel, iterations=1)
#dilated_image = edges
dilated_image_3D = np.dstack((dilated_image, dilated_image, dilated_image))

blue_channel, green_channel, red_channel = cv2.split(original_image)

blue_smoothed_image_Q = cv2.blur(blue_channel, (3, 3))
green_smoothed_image_Q = cv2.blur(green_channel, (3, 3))
red_smoothed_image_Q = cv2.blur(red_channel, (3, 3))

mask1 = (blue_smoothed_image_Q >= 0) & (blue_smoothed_image_Q <= 39)
blue_smoothed_image_Q[mask1] = 0
mask2 = (blue_smoothed_image_Q >= 40) & (blue_smoothed_image_Q <= 79)
blue_smoothed_image_Q[mask2] = 55
mask3 = (blue_smoothed_image_Q >= 80) & (blue_smoothed_image_Q <= 119)
blue_smoothed_image_Q[mask3] = 110
mask4 = (blue_smoothed_image_Q >= 120) & (blue_smoothed_image_Q <= 179)
blue_smoothed_image_Q[mask4] = 165
mask5 = (blue_smoothed_image_Q >= 180) & (blue_smoothed_image_Q <= 239)
blue_smoothed_image_Q[mask5] = 220
mask6 = (blue_smoothed_image_Q >= 240) & (blue_smoothed_image_Q <= 255)
blue_smoothed_image_Q[mask6] = 255

mask1 = (green_smoothed_image_Q >= 0) & (green_smoothed_image_Q <= 39)
green_smoothed_image_Q[mask1] = 0
mask2 = (green_smoothed_image_Q >= 40) & (green_smoothed_image_Q <= 79)
green_smoothed_image_Q[mask2] = 55
mask3 = (green_smoothed_image_Q >= 80) & (green_smoothed_image_Q <= 119)
green_smoothed_image_Q[mask3] = 110
mask4 = (green_smoothed_image_Q >= 120) & (green_smoothed_image_Q <= 179)
green_smoothed_image_Q[mask4] = 165
mask5 = (green_smoothed_image_Q >= 180) & (green_smoothed_image_Q <= 239)
green_smoothed_image_Q[mask5] = 220
mask6 = (green_smoothed_image_Q >= 240) & (green_smoothed_image_Q <= 255)
green_smoothed_image_Q[mask6] = 255

mask1 = (red_smoothed_image_Q >= 0) & (red_smoothed_image_Q <= 39)
red_smoothed_image_Q[mask1] = 0
mask2 = (red_smoothed_image_Q >= 40) & (red_smoothed_image_Q <= 79)
red_smoothed_image_Q[mask2] = 55
mask3 = (red_smoothed_image_Q >= 80) & (red_smoothed_image_Q <= 119)
red_smoothed_image_Q[mask3] = 110
mask4 = (red_smoothed_image_Q >= 120) & (red_smoothed_image_Q <= 179)
red_smoothed_image_Q[mask4] = 165
mask5 = (red_smoothed_image_Q >= 180) & (red_smoothed_image_Q <= 239)
red_smoothed_image_Q[mask5] = 220
mask6 = (red_smoothed_image_Q >= 240) & (red_smoothed_image_Q <= 255)
red_smoothed_image_Q[mask6] = 255

color_image_Q = np.dstack((blue_smoothed_image_Q, green_smoothed_image_Q, red_smoothed_image_Q))

mask = dilated_image_3D == 255
color_image_Q[mask] = 0

merged_image = np.hstack((original_image, color_image_Q))

cv2.imshow('Gray Image', merged_image)
cv2.waitKey(0)