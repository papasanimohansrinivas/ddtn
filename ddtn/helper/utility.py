#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:39:44 2017

@author: nsde
"""
#%%
try:
    import cPickle as pkl
except:
    import pickle as pkl
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.client import device_lib 

#%%
def gpu_support():
    """ Checks for GPU and CUDA support """
    test1 = check_for_gpu()
    test2 = check_cuda_support()
    return (test1 and test2)

#%%
def check_for_gpu():
    """ Check if tensorflow has detected a GPU """
    devices = device_lib.list_local_devices()
    gpu = False
    for d in devices:
        if d.device_type == "GPU": gpu=True
    return gpu

#%%
def check_cuda_support():
    """ Check if tensorflow was build with CUDA """
    return tf.test.is_built_with_cuda()

#%%
def make_hashable(arr):
    """ Make an array hasable. In this way we can use built-in functions like
        set(...) and intersection(...) on the array
    """
    return tuple([tuple(r.tolist()) for r in arr])

#%%
def load_obj(name):
    """ Function for saving a variable as a pickle file """
    with open(name + '.pkl', 'rb') as f:
        return pkl.load(f)

#%%
def save_obj(obj, name):
    """ Function for loading a pickle file """
    with open(name + '.pkl', 'wb') as f:
        pkl.dump(obj, f, pkl.HIGHEST_PROTOCOL)

#%%
def get_path(file):
    """ Get the path of the input file """
    return os.path.realpath(file)

#%%
def get_dir(file):
    """ Get directory of the input file """
    return os.path.dirname(os.path.realpath(file))

#%%
def load_basis():
    """ Load a pre-calculated CPAB basis. See transformer/setup_CPAB_transformer
        for more information on this.
    """
    basis_loc = get_dir(__file__) + '/../cpab_basis'
    try:
        basis = load_obj(basis_loc)
    except:
        raise ValueError('call setup_CPAB.py first')
    return basis

#%%
def debug_printer(string):
    """ Small debug function """
    print('\n')
    print(70*'-')
    print(string)
    print(70*'-')
    print('\n')

#%%
def get_cat():
    """ Get cat image """
    direc = get_dir(__file__)
    return plt.imread(direc + '/../cat.jpg')

#%%
def show_images(images, cols='auto', title=None, scaling=False):
    """ Display a list of images in a single figure with matplotlib.
    
    Arguments
        images: List/tensor of np.arrays compatible with plt.imshow.
    
        cols (Default = 'auto'): Number of columns in figure (number of rows is 
                                 set to np.ceil(n_images/float(cols))).
        
        title: One main title for the hole figure
            
        scaling (Default = False): If True, will rescale the figure by the
                number of images. Good if one want to show many.
    """
    n_images = len(images)
    print(n_images)
    cols = np.round(np.sqrt(n_images)) if cols=='auto' else cols
    rows = np.ceil(n_images/float(cols))
    fig = plt.figure()
    if type(title)==str: fig.suptitle(title, fontsize=20)
    for n, image in enumerate(images):
        a = fig.add_subplot(cols, rows, n + 1)
        if image.ndim == 2: plt.gray()
        a.imshow(image)
        a.axis('on')
        a.axis('equal')
        a.set_xticklabels([])
        a.set_yticklabels([])
    if scaling: fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    fig.subplots_adjust(wspace=0, hspace=0)
    fig.savefig("lets_see2.png")
    print(fig.canvas.get_supported_filetypes())
    # plt.plot()
    plt.imshow(images[0])
    
#%%1
if __name__ == '__main__':
    im = get_cat()
    im = np.tile(im, (10, 1, 1, 1))
    show_images(im)
    
