import os

# here (https://github.com/pytorch/vision/tree/master/torchvision/models) to find the download link of pretrained models

root = '..\\pretrained'
res101_path = os.path.join(root, 'ResNet', 'resnet101-63fe2227.pth')
res152_path = os.path.join(root, 'ResNet', 'resnet152-394f9c45.pth')
inception_v3_path = os.path.join(root, 'Inception', 'inception_v3_google-0cc3c7bd.pth')
vgg19_bn_path = os.path.join(root, 'VggNet', 'vgg19_bn-c79401a0.pth')
vgg16_path = os.path.join(root, 'VggNet', 'vgg16_bn-6c64b313.pth')
dense201_path = os.path.join(root, 'DenseNet', 'densenet201-c1103571.pth')

'''
vgg16 trained using caffe
visit this (https://github.com/jcjohnson/pytorch-vgg) to download the converted vgg16
'''
vgg16_caffe_path = os.path.join(root, 'VggNet', 'vgg16-caffe.pth')
