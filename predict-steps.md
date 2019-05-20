# Steps to Make Image Predictions

## Dependencies

- [Python](https://www.python.org/)
- [PIL](https://pillow.readthedocs.io/en/stable/)
- [Numpy](https://www.numpy.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [tensorflow](https://www.tensorflow.org/)
- [pandas](https://pandas.pydata.org/)

## Classify Images

1. To classify a single image:
    1. Open console application
    2. Type ```python predict.py path/to/image-file```
    3. Model will return a numpy array of shape (1, 2)
    4. The first number of the inner array is the probability that the image is not a chemical structure, the second number is probability that it is a chemical structure
2. To classify several images:
    1. Move all images you want to classify to a certain directory
    2. Open console application
    3. Type ```python batch-predict.py -i path/do/directory-containing-images -r path/to/file-where-to-write-results.csv```
    4. All results will be written to the file indicated in the -r argument with the following fields
        - File path
        - Negative probability
        - Positive probability
