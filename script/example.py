#!/usr/bin/env python

import tensorflow as tf

import numpy as np
import scipy

import matplotlib.pyplot as plt
%matplotlib inline

import time

from urllib.request import urlopen  # Python 3+ version (instead of urllib2)
import os, sys

fLASS_DIR='./images/cars'


slim_models_dir = 'model/tensorflow_zoo'

if not tf.gfile.Exists(slim_models_dir):
    print("Creating model/tensorflow_zoo directory")
    tf.gfile.MakeDirs(slim_models_dir)
if not tf.gfile.Exists(os.path.join(slim_models_dir, 'models', 'README.md')):
    print("Cloning tensorflow model zoo under %s" % (slim_models_dir, ))
    !pushd model/tensorflow_zoo; git clone https://github.com/tensorflow/models.git; popd

sys.path.append("model/tensorflow_zoo/models/slim")
