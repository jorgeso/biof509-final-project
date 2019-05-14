from os import listdir
import argparse
import pandas as pd
import random
import numpy as np
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to directory containing image files")
ap.add_argument("-otr", "--outtrain", required=True,
	help="path to output directory of training data")
ap.add_argument("-ote", "--outtest", required=True,
	help="path to output directory of testing data")
ap.add_argument("-ntr", "--numtrain", required=True,
	help="number of items to copy")
ap.add_argument("-nte", "--numtest", required=True,
	help="number of items to copy")

args = vars(ap.parse_args())

inputDirectoryPath = args["input"]
outputTest = args["outtest"]
outputTrain = args["outtrain"]
numTestingData = int(args["numtest"])
numTrainingData = int(args["numtrain"])

fileNames = listdir(inputDirectoryPath)

fileNamesDf = pd.DataFrame(fileNames)

fileNamesIndexes = fileNamesDf.index.values
addedIndexes = np.empty(0, dtype=int)

numTestingAdded = 0
numTrainAdded = 0

while numTestingAdded < numTestingData:
    random_index = random.choice(fileNamesIndexes)

    if random_index not in addedIndexes:
        copiedPath = shutil.copy(inputDirectoryPath + '/' + fileNamesDf.iloc[random_index, 0], outputTest)
        print(copiedPath + ' copied to test')
        print('numTestingAdded: ' + str(numTestingAdded))
        addedIndexes = np.append(addedIndexes, [random_index])
        numTestingAdded = len(listdir(outputTest))

while numTrainAdded < numTrainingData:
    random_index = random.choice(fileNamesIndexes)

    if random_index not in addedIndexes:
        copiedPath = shutil.copy(inputDirectoryPath + '/' + fileNamesDf.iloc[random_index, 0], outputTrain)
        print(fileNamesDf.iloc[random_index, 0] + ' copied to train')
        print('numTrainAdded: ' + str(numTrainAdded))
        addedIndexes = np.append(addedIndexes, [random_index])
        numTrainAdded = len(listdir(outputTrain))

print('numTestingAdded: ' + str(numTestingAdded))
print('numTrainAdded: ' + str(numTrainAdded))