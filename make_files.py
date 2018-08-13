import os

tf = open('train.txt', 'w+')
vf = open('test.txt', 'w+')

train_path = '/Users/arunprakash/Documents/GitHub/darknet/train/'
test_path = '/Users/arunprakash/Documents/GitHub/darknet/test/'
for i in os.listdir(train_path):
    if '.jpg' in i:
        tf.write(train_path + i + '\n')
tf.close()

for i in os.listdir(test_path):
    if '.jpeg' in i:
        vf.write(test_path + i + '\n')
vf.close()
