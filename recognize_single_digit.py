import cv2
import numpy
from sys import argv
from joblib import load
from warnings import filterwarnings
from skimage.transform import resize

filterwarnings('ignore')

classifier_path = "./classifier.joblib"
img_path = "./digit5.jpg"

classifier_img_size = (26,18)

def getDigitString():

    clf = load(classifier_path)

    # Preprocessing
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
    img_resized = resize(gray_img, classifier_img_size, anti_aliasing=True, mode='reflect')

    flat_data = numpy.expand_dims(img_resized.flatten(),axis=0)

    # Classification
    result = clf.predict(flat_data)[0]

    return result
    

if __name__ == '__main__':
    if len(argv)>1:
        img_path = argv[1]
    print(getDigitString())



