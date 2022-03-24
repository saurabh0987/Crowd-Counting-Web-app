# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:39:16 2022

@author: saura
"""
import h5py
import scipy.io as io
import PIL.Image as Image
import numpy as np
import os
import glob
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter 
import scipy
import json
import torchvision.transforms.functional as F
from matplotlib import cm as CM
from image import *
from model import CSRNet
import torch
import pickle
import os
#%matplotlib inline

import os    
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from torchvision import datasets, transforms
transform=transforms.Compose([
                       transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225]),
                   ])

#new image data
from matplotlib import cm as c
def Count(img):
    #Unpickeling Model_object
    path = os.path.dirname(__file__)
    my_file = path+'/model_object'
    dbfile = open(my_file, 'rb')     
    model = pickle.load(dbfile)
    dbfile.close()
    
    
    img = transform(Image.open(img).convert('RGB'))
    output = model(img.unsqueeze(0))
    print("Predicted Count : ",int(output.detach().cpu().sum().numpy()))
    temp = np.asarray(output.detach().cpu().reshape(output.detach().cpu().shape[2],output.detach().cpu().shape[3]))
    print("Original Image")
    #plt.imshow(plt.imread(img))
    #plt.show()
    print(type(img))
    return (int(output.detach().cpu().sum().numpy()),img)
    
