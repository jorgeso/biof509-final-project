# Model Training Steps

## Dependencies

- [Python](https://www.python.org/)
- [PIL](https://pillow.readthedocs.io/en/stable/)
- [Numpy](https://www.numpy.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [tensorflow](https://www.tensorflow.org/)
- [pandas](https://pandas.pydata.org/)

## Download and Organize Images

1. If you need images to train your model, you can follow the steps on [this blog](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/)
2. Create a folder that will hold all your images
3. Inside the folder above, organize your images so that different classes are in different folders (e.g., if you want to classify images of dogs and cats, then create two sub-folders: "dogs," and "cats")

## Train Model

1. Open your console application, type ```python train.py -i path/to/images/folder -it 3000 -m name-for-your-model``` and press enter
2. A few files will be created with the model name you entered
