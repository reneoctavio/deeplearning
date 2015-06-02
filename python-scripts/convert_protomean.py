import caffe
import numpy as np
import sys

blob = caffe.proto.caffe_pb2.BlobProto()
data = open("caltech101_mean.binaryproto", "rb").read()
blob.ParseFromString(data)
nparray = np.array( caffe.io.blobproto_to_array(blob) )
f = file("mean.npy","wb")
np.save(f,nparray[0])
f.close()