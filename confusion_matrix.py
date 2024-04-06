"""
Thomas Roberts
CS 4732
Professor Karakaya
March 28, 2024

Program Description: This program will generate the learning model with the best
accuracy based on the results from main.py, and then generate a confusion
matrix from that learning model.
"""

import tensorflow
import numpy
from tensorflow.keras.applications import vgg19
from transfer_learning import Transfer_Learning as tl

training_ds, validation_ds = tensorflow.keras.utils.image_dataset_from_directory("dataset\\Train",
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

# base
vgg_base = vgg19.VGG19(include_top=False)

# creating and saving top model
model_1 = tl.adjust_model(vgg_base)
model_1 = tl.train_model(model_1, training_ds, validation_ds, 0.001, 4, 0.9)

# creating training labels
training_labels = numpy.concatenate([y for x, y in training_ds], axis=0)
train_p = model_1.predict(training_ds)
training_pred = numpy.round(train_p, 0)

# creating training labels
valid_labels = numpy.concatenate([y for x, y in validation_ds], axis=0)
val_p = model_1.predict(training_ds)
valid_pred= numpy.round(val_p, 0)

# creating training labels
test_labels = numpy.concatenate([y for x, y in testing_ds], axis=0)
test_p = model_1.predict(training_ds)
test_pred = numpy.round(test_p, 0)

# matrices
train_matrix = tensorflow.math.confusion_matrix(training_labels, training_pred, 2)
print("Training Matrix: " + str(train_matrix))

valid_matrix = tensorflow.math.confusion_matrix(valid_labels, valid_pred, 2)
print("Validation Matrix: " + str(valid_matrix))

test_matrix = tensorflow.math.confusion_matrix(test_labels, test_pred, 2)
print("Testing Matrix: " + str(test_matrix))

