# biof509 Final project

This project was developed for a machine learning class at [FAES](https://faes.org/) at the National Institutes of Health. It consists of developing a convolutional neural network (CNN) for binary image classification, with the purpose of classifying images into two classes: chemical scructure, and not chemical structure.

## Process

Developing this model required several steps which included: acquiring data, data pre-processing, cross-validation, model training, and making predictions

### Acquiring Data

To develop this model, I had to acquire two types of images: 1) chemical structure images, and 2) images that may pass as chemical structures to a CNN. I was able to get the chemical structure images from a private source, and unfortunately I'm not able to include them in this repository.

For the not-chemical-structure images, I had to be a little more creative. I [found a script](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/) to help me download images from Google. Essentially, all I had to was enter search terms into Google Images that would produce the desired results (e.g., "diagram", "flowchart"), run the script in the browser download all the image URLs, and then run a python script to download all images.

### Data Pre-Processing

In order to make sure that the CNN didnn't pick up on any little subtle, unimportant, differences 
