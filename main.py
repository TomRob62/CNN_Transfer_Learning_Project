"""
Thomas Roberts
CS 4732
Professor Karakaya
March 28, 2024

This program will try to implement a CNN with GoogLeNet, VGG, and ResNet50 and
compare the results
"""

import tensorflow
from tensorflow.keras.applications import resnet_v2
from tensorflow.keras.applications import vgg19
from transfer_learning import Transfer_Learning as tl


# calling dataset directory creation method. 
tl.create_dataset("Test")
tl.create_dataset("Train")

# creating dataset object
dataset, validation = tensorflow.keras.utils.image_dataset_from_directory("dataset\\Train",
                                                              labels = 'inferred',
                                                              label_mode = 'categorical',
                                                              color_mode = 'rgb',
                                                              seed = 7,
                                                              validation_split = 0.30,
                                                              subset = 'both',
                                                              batch_size = 16)
testing_ds = tensorflow.keras.utils.image_dataset_from_directory("dataset\\Test",
                                                              labels = 'inferred',
                                                              label_mode = 'categorical',
                                                              color_mode = 'rgb',
                                                              seed = 7,
                                                              batch_size = 16)

resnet_model = resnet_v2.ResNet50V2(include_top=False)
resnet_model = tl.adjust_model(resnet_model)
resnet_model = tl.train_model(resnet_model, dataset, validation, max_epoch=5)
accuracy = resnet_model.evaluate(testing_ds, verbose=0)
print("\nResnet Metrics: ")
print(accuracy)

vgg_model = vgg19.VGG19(include_top=False)
vgg_model = tl.adjust_model(vgg_model)
vgg_model = tl.train_model(vgg_model, dataset, validation, max_epoch=5)
accuracy = vgg_model.evaluate(testing_ds, verbose=0)
print("\nVGG Metrics:")
print(accuracy)
