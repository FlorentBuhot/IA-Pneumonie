# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import matplotlib.image
import os
import pandas as pd
from matplotlib import image as mpimg
import skimage.transform as skimg


def load_image_shape(folder):
    images = [2]
    for filename in os.listdir(folder):
        img = mpimg.imread(os.path.join(folder,filename))
        if img is not None:
            images[0].append(img.shape[0])
            images[1].append(img.shape[1])
    return images

def load_image(folder,sp):
    images = []
    for filename in os.listdir(folder):
        img = mpimg.imread(os.path.join(folder,filename))
        if img is not None:
            re = skimg.resize(img,(1400,800))
            print(re.shape)
            images.append(re)
    return images

test = load_image_shape("Ressource/test/NORMAL")
print(test)
#df = pd.DataFrame(test)
#print(df.shape[0])


