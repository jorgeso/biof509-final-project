import numpy as np
import os
import pandas as pd
from os import listdir
import argparse
import model
import numpy as np
import image_modifier
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to directory containing image files")
ap.add_argument("-r", "--results", required=True,
	help="path to results csv file")

args = vars(ap.parse_args())

inputDirectoryPath = args["input"]
resultsCsvFilePath = args["results"]

fileNames = listdir(inputDirectoryPath)
columns = ['file_path','negative','positive']
df =  pd.DataFrame(columns=columns)

for fileName in fileNames:
    filename = inputDirectoryPath +'/' + fileName
    image_size=128
    try:
        squaredImage = image_modifier.squareImage(Image.open(filename, 'r'))
        # Reading the image using OpenCV
        image = np.array(squaredImage)
        result = model.predict(image, image_size, 'classification-model.meta', 2)
        negative = result[0, 0]
        positive = result[0, 1]
        rowDf = pd.DataFrame([[filename,negative,positive]], columns=columns)
        df = df.append(rowDf)
        df.to_csv(path_or_buf=resultsCsvFilePath)
        print(result)
        print("Prediction complete for {}".format(fileName))
    except:
        print("Not able to make prediction for {}".format(fileName))