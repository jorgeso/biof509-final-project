# biof509 Final project

This project was developed for a machine learning class at [FAES](https://faes.org/) at the National Institutes of Health. It consists of developing a convolutional neural network (CNN) for binary image classification, with the purpose of classifying images into two classes: chemical scructure (positive), and not chemical structure (negative).

## Process

Developing this model required several steps which included: acquiring data, data pre-processing, cross-validation, model training, model testing, and making predictions

### Acquiring Data

To develop this model, I had to acquire two types of images: 1) chemical structure images, and 2) images that may pass as chemical structures to a CNN. I was able to get the chemical structure images from a private source, and unfortunately I'm not able to include them in this repository.

For the not-chemical-structure images, I had to be a little more creative. I [found a script](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/) to help me download images from Google. Essentially, all I had to was enter search terms into Google Images that would produce the desired results (e.g., "diagram", "flowchart"), run the script in the browser download all the image URLs, and then run a python script to download all images.

### Data Pre-Processing

To make sure that the CNN didnn't pick up on any unimportant and subtle patterns to differentiate between the classes, I made all images as similar as possible. First, I removed all transparent background and replaced it with white background. Second, I made all images square by adding white padding where necessary. And third, I resized them to 128 by 128 pixels. This process was performed for all images used for training, and to all images used for testing.

### Cross-Validation

The initial data consisted of around 13,500 positive images and around 3,000 negative images. Of this data, four thousand totla images were used to train and test the model (two thousand of each class). These images were divided as follows: 80% train, and 20% test. And the train data was further divided into 80% train and 20% validate. In order to divide the data, a custom python script was developed that randomly selected the images.

As of this writing, the model was only trained and tested once.

### Model Training

To train this model, I followed the instructions and recommended architecture on [this blog](https://cv-tricks.com/tensorflow-tutorial/training-convolutional-neural-network-for-image-classification/), which consists of six layers: three convolutional layers, one flattened layer, and two fully connected layers - including the output layer. The shape of the filters for each convolutional layer is 3 (width) x 3 (height) x 3 (number of channels) and 32 filters for the first two layers and 64 for the third layer. The initial set of weights are randomly selected, but follow a normal distribution. These weights are adjusted during training until the cost function produces minimal results.

The trained model is saved in a series of files in the root directory and in the tmp directory
