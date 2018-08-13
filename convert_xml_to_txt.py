import xml.etree.ElementTree as ET
import os
def get_coords():
    coords = []
    for bbox in root.iter('object'):
        for i in bbox.findall('bndbox'):
            coords.append([float(i.find('xmin').text), float(i.find('xmax').text), float(i.find('ymin').text), float(i.find('ymax').text)])
    return coords

def convert(cl, siz, coords):
    pre_cls=['seal','noise', 'pageno', 'tag']
    dw = 1./siz[0]
    dh = 1./siz[1]
    x = (coords[0] + coords[1])/2.0
    y = (coords[2] + coords[3])/2.0
    w = coords[1] - coords[0]
    h = coords[3] - coords[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (pre_cls.index(cl),x,y,w,h)

ann_path='/Users/arunprakash/Documents/L&D/Tensorflow/annotations/sealasroiold/ann/'
for fl in os.listdir(ann_path):
    if '.xml' in fl:
        fnme = fl[:-4]
        print(fnme)

        tree = ET.parse(ann_path + fnme + '.xml')
        root = tree.getroot()

        for size in root.findall('size'):
            sz = (int(size.find('width').text), int(size.find('height').text))
        cls = []
        for name in root.findall('object'):
            cls.append(name.find('name').text)

        seal_co = get_coords()
        myf = open(ann_path + 'txtfiles/' + fnme + '.txt', 'w+')
        for num,cl in enumerate(cls):
            dt = str(convert(cl,sz,seal_co[num]))
            myf.write(dt[1:-1].replace(',', '') + '\n')
        myf.close()
