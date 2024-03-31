"""
Thomas Roberts
CS 4732
Professor Karakaya
March 28, 2024

This program contains the helper methods used to build a CNN
network with transfer learning
"""

import os
import shutil
import tensorflow

class Transfer_Learning:
    def create_dataset(sub_directory: str) -> str:
        """
        Sorts the files in a directory into two files for categorization.
        
            This method is specific to DS_IDRID, so the two files categories
            are DR and NONDR.

        Returns
        -------
        str
            the name of the new folder
        """
        # current directory
        curr_dir = os.getcwd()

        #source directory
        source_dir = curr_dir + "\\DS_IDRID\\" + sub_directory

        #destination directory
        dest_dir = curr_dir + "\\dataset\\" + sub_directory
    
        # creating subdirectory for DR and NONDR
        if not os.path.exists((dest_dir + "\\DR")):
            os.mkdir((dest_dir + "\\DR"))
            os.mkdir((dest_dir + "\\NONDR"))

        # Sorting each file into my dataset
        for file_str in os.listdir(source_dir):
            # parsing category number from file name
            index = file_str.index("-") # using '-' as identifier 
            category = file_str[index+1]
            category = int(category) # int category

            # source path for current image
            image_src = (source_dir + "\\" + file_str)

            if category == 3 or category == 4: # DR category
                # destination path for current image
                image_dest = (dest_dir + "\\DR\\" + file_str)
                shutil.copyfile(image_src, image_dest)
            elif category == 0: # non DR category
                image_dest = (dest_dir + "\\NONDR\\" + file_str)
                shutil.copyfile(image_src, image_dest)
        # end for loop
        return dest_dir
    # end definition create_dataset

    def adjust_model(model: tensorflow.keras.Model) -> tensorflow.keras.Model:
        """
        Helper method that adjust a prebuilt model like googlenet
        to fit this program objective
        """
        # freezing the base layers as we don't want to alter their weights
        for layer in model.layers:
            layer.trainable = False

        # adding custom layers to model to fit out dataset
        my_model = tensorflow.keras.Sequential()
        my_model.add(model)
        my_model.add(tensorflow.keras.layers.Conv2D(64, (3,3), activation = "relu"))
        my_model.add(tensorflow.keras.layers.Flatten())
        my_model.add(tensorflow.keras.layers.Dense(256, activation='relu'))
        my_model.add(tensorflow.keras.layers.Dropout(0.5))
        my_model.add(tensorflow.keras.layers.Dense(2, activation='softmax'))
        return my_model
    # end of definition adjust model

    def train_model(model, training_ds, validation_ds, learning_r = 0.005, max_epoch = 10):
        optimize = tensorflow.keras.optimizers.SGD(learning_rate = learning_r, momentum = 0.9)
        model.compile(loss='categorical_crossentropy', optimizer=optimize, metrics=['accuracy'])
        history = model.fit(training_ds, epochs = max_epoch, validation_data=validation_ds)
        return model
    # end of definition train_model     

# end of class Transer_Learning