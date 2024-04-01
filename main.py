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
from my_statistics import My_Statistics


# calling dataset directory creation method. 
tl.create_dataset("Test")
tl.create_dataset("Train")

# creating dataset object
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

learning_rates = [0.0001, 0.00025, 0.0005, 0.001, 0.005, 0.01]
momentum = [0, 0.3, 0.6, 0.9]

for lr in learning_rates:
    for moment in momentum:
        for e in range(1, 6):
            resnet_model = resnet_v2.ResNet50V2(include_top=False)
            resnet_model = tl.adjust_model(resnet_model)
            resnet_model = tl.train_model(resnet_model, training_ds, validation_ds, max_epoch=e)
            accuracy = resnet_model.evaluate(testing_ds, verbose=0)

            stats = My_Statistics(e, lr, "resnet", moment)
            stats.training_loss, stats.training_acc = resnet_model.evaluate(training_ds, verbose=0)
            stats.test_loss, stats.test_acc = resnet_model.evaluate(testing_ds, verbose=0)
            stats.valid_loss, stats.valid_acc = resnet_model.evaluate(validation_ds, verbose=0)
            stats.print_statistics()
            stats.save_statistics()

            vgg_model = vgg19.VGG19(include_top=False)
            vgg_model = tl.adjust_model(vgg_model)
            vgg_model = tl.train_model(vgg_model, training_ds, validation_ds, max_epoch=e)
            accuracy = vgg_model.evaluate(testing_ds, verbose=0)

            stats = My_Statistics(e, lr, "vgg", moment)
            stats.training_loss, stats.training_acc = vgg_model.evaluate(training_ds, verbose=0)
            stats.test_loss, stats.test_acc = vgg_model.evaluate(testing_ds, verbose=0)
            stats.valid_loss, stats.valid_acc = vgg_model.evaluate(validation_ds, verbose=0)
            stats.print_statistics()
            stats.save_statistics()

