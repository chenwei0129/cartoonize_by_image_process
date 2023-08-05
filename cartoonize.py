import cv2
import numpy as np
import os

def gen_edge_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    median_filtered_image = cv2.medianBlur(gray_image, 5)

    edges = cv2.Canny(median_filtered_image, 70, 140)
    cv2.imshow('Original Image', edges)
    cv2.waitKey(0)

    kernel = np.ones((2, 2), np.uint8)

    dilated_image = cv2.dilate(edges, kernel, iterations=2)
    cv2.imshow('Original Image', dilated_image)
    cv2.waitKey(0)
    
    dilated_image_3D = np.dstack((dilated_image, dilated_image, dilated_image))
    
    return dilated_image_3D

def quantize(image):
    smoothed_image = cv2.blur(image, (3, 3))
    
    mask1 = (smoothed_image >= 0) & (smoothed_image <= 31)
    mask2 = (smoothed_image >= 32) & (smoothed_image <= 63)
    mask3 = (smoothed_image >= 64) & (smoothed_image <= 95)
    mask4 = (smoothed_image >= 96) & (smoothed_image <= 127)
    mask5 = (smoothed_image >= 128) & (smoothed_image <= 159)
    mask6 = (smoothed_image >= 160) & (smoothed_image <= 191)
    mask7 = (smoothed_image >= 192) & (smoothed_image <= 223)
    mask8 = (smoothed_image >= 224) & (smoothed_image <= 255)
    
    smoothed_image[mask1] = 0
    smoothed_image[mask2] = 47
    smoothed_image[mask3] = 80
    smoothed_image[mask4] = 112
    smoothed_image[mask5] = 144
    smoothed_image[mask6] = 176
    smoothed_image[mask7] = 208
    smoothed_image[mask8] = 255
    
    return smoothed_image

def gen_quantize_image(image):
    blue_channel, green_channel, red_channel = cv2.split(image)

    blue_smoothed_image_Q = quantize(blue_channel)
    green_smoothed_image_Q = quantize(green_channel)
    red_smoothed_image_Q = quantize(red_channel)

    color_image_Q = np.dstack((blue_smoothed_image_Q, green_smoothed_image_Q, red_smoothed_image_Q))
    
    return color_image_Q

def combine_image(edge_image, color_image):
    mask = (edge_image == 255)
    color_image[mask] = 0
    
    return color_image

folder_path = "./images/"
number = 0
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        original_image = cv2.imread(file_path)
        
        edge_image = gen_edge_image(original_image)

        color_image_Q = gen_quantize_image(original_image)

        cartoon_image = combine_image(edge_image, color_image_Q)
        
        output_path = "./cartoon/" + str(number).zfill(3) + ".jpg"
        cv2.imwrite(output_path, cartoon_image)
        number = number + 1
