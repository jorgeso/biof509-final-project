import os,glob,cv2
import sys,argparse
import pandas as pd
import image_modifier
from PIL import Image
import model
import numpy as np

# First, pass the path of the image
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path=sys.argv[1] 
filename = dir_path +'/' +image_path
image_size=128
squaredImage = image_modifier.squareImage(Image.open(filename, 'r'))
# Reading the image using OpenCV
image = np.array(squaredImage)
results = model.predict(image, image_size, 'classification-model.meta', 2)
print(results)