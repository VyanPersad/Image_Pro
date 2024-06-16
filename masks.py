import numpy as np
import cv2

#These functions return an image

lower_array = []
upper_array = []

def shadowMsk(image, lower_array, upper_array):
    #Shadow Mask
    #0,0,0
    #180, 50,15
    converted_c = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lshad = np.array(lower_array, dtype="uint8")
    ushad = np.array(upper_array, dtype="uint8")
    shadow_mask = cv2.inRange(converted_c, lshad, ushad)
    #This should show the shadowed region with a green tint.
    img_w_shadow_highlight = cv2.bitwise_and(converted_c, converted_c, mask=~shadow_mask)
    return img_w_shadow_highlight

def HSVskinMask(image,lower_array, upper_array):
    #3,15,10
    #20,255,255
    lower = np.array(lower_array, dtype="uint8")
    upper = np.array(upper_array, dtype="uint8")

    converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations=2)
    skinMask = cv2.dilate(skinMask, kernel, iterations=2)
    # blur the mask to help remove noise
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    # apply the mask to the original image
    skin = cv2.bitwise_and(image, image, mask=skinMask)
    # Find contours in the skin mask
    contours, _ = cv2.findContours(skinMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Initialize a list to store bounding boxes of non-black/skin regions
    non_black_boxes = []
    # Loop over the contours
    for contour in contours:
        # Get bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 100:
            non_black_boxes.append((x, y, w, h))
        
    # Create a copy of the original skin image
    skin_cropped = skin.copy()
    # Draw bounding boxes on the copy
    # This only draws the reactangle bounding boxes
    for box in non_black_boxes:
        x, y, w, h = box
        #img output,upper left, lower right, BGR Color, thickness
        cv2.rectangle(skin_cropped, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Determine Largest Contour
    # Get largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    largest_contour_mask = np.zeros_like(skinMask)
    cv2.drawContours(largest_contour_mask, [largest_contour], 0, 255, thickness=cv2.FILLED)

    # Apply the mask to the original image
    largest_contour_image = cv2.bitwise_and(image, image, mask=largest_contour_mask) 

    return largest_contour_image

def YCbCrskinMask(image,lower_array, upper_array):
    #0,138,67
    #255,173,133

    lower = np.array(lower_array, dtype="uint8")
    upper = np.array(upper_array, dtype="uint8")

    converted = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    skinMask = cv2.inRange(converted, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations=2)
    skinMask = cv2.dilate(skinMask, kernel, iterations=2)
    # blur the mask to help remove noise
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    # apply the mask to the original image
    skin = cv2.bitwise_and(image, image, mask=skinMask)
    # Find contours in the skin mask
    contours, _ = cv2.findContours(skinMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Initialize a list to store bounding boxes of non-black/skin regions
    non_black_boxes = []
    # Loop over the contours
    for contour in contours:
        # Get bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 100:
            non_black_boxes.append((x, y, w, h))
        
    # Create a copy of the original skin image
    skin_cropped = skin.copy()
    # Draw bounding boxes on the copy
    # This only draws the reactangle bounding boxes
    for box in non_black_boxes:
        x, y, w, h = box
        #img output,upper left, lower right, BGR Color, thickness
        cv2.rectangle(skin_cropped, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Determine Largest Contour
    # Get largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    largest_contour_mask = np.zeros_like(skinMask)
    cv2.drawContours(largest_contour_mask, [largest_contour], 0, 255, thickness=cv2.FILLED)

    # Apply the mask to the original image
    largest_contour_image = cv2.bitwise_and(image, image, mask=largest_contour_mask) 

    return largest_contour_image
