#perceptual hashing
import cv2 
import imagehash
import os
from PIL import Image
# import matplotlib.pyplot as plt
# Define the path to the directory containing the images
path = 'C:\\Users\\arif shaikh\\OneDrive\\Desktop\\C Tutorials COURSE\\.vscode\\pyproject\\Airbnb Data\\Test Data\\kitchen'

# Create a dictionary to store the image hashes
image_hashes = {}

# Loop through the images in the directory
for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image using OpenCV
        image = cv2.imread(os.path.join(path, filename))

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Compute the hash of the image using the imagehash library
        hash = imagehash.phash(Image.fromarray(gray))

        # Store the hash in the dictionary
        if hash in image_hashes:
            image_hashes[hash].append(filename)
        else:
            image_hashes[hash] = [filename]

# Loop through the dictionary and print the images with the same hash
for hash, filenames in image_hashes.items():
    if len(filenames) > 1:
        print("Images with hash", hash)
        for filename in filenames:
            print(filename)
       
        



#This code loads each image in the directory, 
# converts it to grayscale, and computes its perceptual hash using the phash() function from the imagehash library. 
# It then stores the hash in a dictionary, with the filenames of images that have the same hash stored in a list. 
# Finally, the code loops through the dictionary and prints the filenames of images that have the same hash, which identifies the duplicate or similar images.
