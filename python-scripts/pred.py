import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Make sure that caffe is on the python path:
caffe_root = '/Users/reneoctavio/caffe/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = '/Users/reneoctavio/Dropbox/UnB/machine-learning/caffe-projects/caltech101/simplenndeploy.prototxt'
PRETRAINED = '/Users/reneoctavio/Dropbox/UnB/machine-learning/caffe-projects/caltech101/lenet_iter_10000.caffemodel'
IMAGE_FILE = '/Users/reneoctavio/Documents/TorchData/Caltech101/101_ObjectCategories/accordion/image_0001.jpg'

caffe.set_mode_cpu()
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load('/Users/reneoctavio/Dropbox/UnB/machine-learning/caffe-projects/caltech101/mean.npy').mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))