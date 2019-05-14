import image_modifier
from os import listdir
import argparse
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to directory containing image files")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")

args = vars(ap.parse_args())

inputDirectoryPath = args["input"]
outputDirectoryPath = args["output"]

fileNames = listdir(inputDirectoryPath)

for fileName in fileNames:
    filePath = inputDirectoryPath + '/' + fileName
    try:
        image = Image.open(filePath, 'r')
        squaredImage = image_modifier.squareImage(image)
        image = image.resize((128, 128))
        image.save(outputDirectoryPath + '/' + fileName)
    except:
        print("[INFO] error processing image {}".format(fileName))