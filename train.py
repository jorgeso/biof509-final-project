import argparse
import model

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to directory containing training images files")
ap.add_argument("-it", "--iterations", required=True,
	help="number of iterations")
ap.add_argument("-m", "--model", required=True,
	help="model name")

args = vars(ap.parse_args())

inputDirectoryPath = args["input"]
num_iterations = int(args["iterations"])
model_name = args["model"]

model.train(inputDirectoryPath, num_iterations, model_name)