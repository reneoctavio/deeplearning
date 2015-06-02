#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

CAFFE=/Users/reneoctavio/caffe
DATA=/Users/reneoctavio/Documents/TorchData/Caltech101/101_ObjectCategories
TOOLS=$CAFFE/build/tools

$TOOLS/compute_image_mean $DATA/caltech101_val_lmdb \
  $DATA/caltech101_mean.binaryproto

echo "Done."