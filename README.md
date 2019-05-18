# biof509 Final project

This project was developed for a machine learning class at [FAES](https://faes.org/), at the National Institutes of Health. It consists of developing a convolutional neural network (CNN) for binary image classification, with the purpose of classifying images into two classes: chemical scructure (positive), and not chemical structure (negative).

This model can serve as an initial check for more complex services/algorigthms that convert images of chemical structures into [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)'s and/or [Molfiles](https://en.wikipedia.org/wiki/Chemical_table_file#Molfile). Two examples are [OSRA](https://cactus.nci.nih.gov/cgi-bin/osra/index.cgi), and Molvec (which can be seen action when you copy-and-paste, or drag an image of a chemical structure into this editor https://ginas.ncats.nih.gov/ginas/app/structure). These services assume the image being passed is that of a chemical structure and perform really well then it is. But they don't perform well when they receive an image that's similar to a structure.

Another use case is the extraction of chemical structures from publications. This model can be used along with OpenCV to process PDFs as images and identify the parts of it that are images of chemical structures. This way, extracted images can be passed to OSRA or Molvec in order to get their alternative formats.

[Click here for steps to train your own model](train-steps.md)

[Click here for steps to make predictions](train-steps.md)

## Process

Developing this model required the following steps: acquiring data, data pre-processing, cross-validation, model training, model testing.

### Acquiring Data

Two types of images were required to develop this model: 1) chemical structure images, and 2) images that may pass as chemical structures to a CNN. I received the chemical structure images from a private source, but unfortunately I'm not able to include them in this repository.

For the negative images, I had to be a little more creative. I [found a script](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/) to help me download images from Google. In summary, I had to enter search terms into Google Images that would produce the desired results (e.g., "diagram", "flowchart"), run the script in the browser (which saved all the image URLs into a text file), and then run a python script to download all images.

### Data Pre-Processing

To make sure that the CNN didnn't pick up on any unimportant and subtle patterns in the images, I had to make sure all images were similar as possible. First, I removed all transparent background and replaced it with white background. Second, I made all images square by adding white padding where necessary. Third, I resized all images to 128 by 128 pixels. And fourth, I normalized the pixel intesities to a range of zero to one (from a range of 0 to 255). This process was performed for all images used for training, and for all images used for testing.

### Cross-Validation

The initial data consisted of around 13,500 positive images and around 3,000 negative images. Of this data, four thousand total images were used to train and test the model (two thousand of each class). And they were divided as follows: 80% training, and 20% testing. The training data was further divided into 80% training and 20% validating. In order to divide the data, a custom python script was developed that randomly selected the images and moved them to separate directories.

As of this writing, the model was only trained and tested once.

### Model Training

To train this model, I followed the instructions and recommended architecture on [this blog](https://cv-tricks.com/tensorflow-tutorial/training-convolutional-neural-network-for-image-classification/), which consisted of six layers: three convolutional layers, one flattened layer, and two fully connected layers - including the output layer. The shape of the filters for each convolutional layer is 3 (width), 3 (height), 3 (number of channels) and 32 filters for the first two layers and 64 filters for the third layer. The initial set of weights are randomly selected, but follow a normal distribution. These weights are adjusted during training until the cost function produces minimal results. The stride for the convolutional layers was set to one.

The trained model is saved in a series of files in the root directory and in the tmp directory.

### Model Testing

After the model was trained, it was tested on eight hundred images (400 positive, and 400 negative) which the model had not seen before. The results are in the predictions_on_test.xlsx file, but the summary is as follows:

| Measurement                     |    Rate     |
|---------------------------------|-------------|
| True Positive Rate (TPN)	      |       0.925 |
| True Negative Rate (TNR)	      |       0.985 |
| Positive Predictive Value (PPV) |	0.984042553 |
| Negative Predictive Value (NPV) | 0.929245283 |

The high rates in the first set of results, along with the high number of 1's in the "negative" column of the results table, may suggest that the model is  overfitting. In order to test this, different models will have to be trained with narrower networks and/or using other methods in general.  

## Next Steps

The obvious next step will be to have more rigorous cross validation to make sure the model is not overfitting. This will entail training new models using different CNN architectures and different methods altogether (like random forest). Also, because this model would be dealing with fairly simple images (compared to complex images like that of faces), it's probably best to add a pre-processing step to convert all images to gray scale, or it may even be very beneficial to change pixel values to binary.