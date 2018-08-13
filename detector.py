import python.darknet
import os, sys
net = python.darknet.load_net(b'cfg/yolov3_tiny_nd.cfg', b'backup/yolov3_tiny_nd_900.weights', 0)
meta = python.darknet.load_meta(b'cfg/obj.data')

im = python.darknet.load_image(b'/Users/arunprakash/Documents/GitHub/darknet/test/lerbatch5.jpg', 0, 0)
res = python.darknet.detect(net, meta, im)
print(res)
