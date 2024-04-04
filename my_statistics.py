"""
    Thomas Roberts
    CS 4732 - 01
    Professor Karakaya
    April 3, 2024

    Program Description: This program handles the statistics/results generated from
    deep learning models. It records optimizer information and results from training.

"""


class Statistics_Object:
    """
    Description: Class that holds the information/statistics for a single model
    such as optimizer information and the results from training

    Attributes
    ----------
    max_epoch
    learning_rate
    batch_size
    moment
    optimizer_name
    model_name
    loss
        list of losses generated
    accuracy
        list of accuracies generated

    Functions
    ---------
    __init__()
    add_accuracy()
    add_loss()
    add_pair()
    __str__()
    """

    # list of attributes for model optimizer
    max_epoch = 0
    learning_rate = 0.01
    batch_size = 32
    momentum = 0.9
    optimizer_name = ""
    model_name = ""

    # variables for storing model results
    # example loss = [['training_loss', 1.0510], ['testing_loss', 0.510351], []'None', 15.0650165]]
    loss = []
    accuracy = []

    def __init__(self, epoch, batch_size, learning_rate, momentum, optimzer, model) -> None:
        """
            Constructor function for statistics object. It holds information for a single 
            model such as optimizer information and results.

            Paramaters
            ----------
            epoch
            batch_size
            learning_rate
            momentum
            name
        """
        self.max_epoch = epoch
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.optimizer_name = optimzer
        self.model_name = model
        self.loss = []
        self.accuracy = []
        return None
    # end of definition __init__

    def add_accuracy(self, accuracy: float, name: str = "None") -> None:
        """
            Creates a list object with the name and accuracy. E.g. ["None", 0.510351]
            and appends it to the class attribute 'accuracy'

            Paramaters
            -----------
            accuracy
            name
                name to identify what the accuracy pertains to
        """
        obj = [name, accuracy]
        self.accuracy.append(obj)
        return None
    # end definition add_accuracy()

    def add_loss(self, loss: float, name: str = "None") -> None:
        """
            Creates a list object with the name and loss. E.g. ["None", 0.510351]
            and appends it to the class attribute 'loss'

            Paramaters
            -----------
            loss
            name
                name to identify what the accuracy pertains to
        """
        obj = [name, loss]
        self.loss.append(obj)
        return None
    # end definition add_loss()

    def add_pair(self, pair: list, name: str = "None") -> None:
        """
            Creates two list objects with name and value (from pair). E.g. ["None", 0.510351]
            and appends it to the class attribute loss and accuracy.

            Paramaters
            -----------
            pair
                [loss, accuracy]
            name
                name to identify what the values pertain to
        """
        obj_loss = [name, pair[0]]
        self.loss.append(obj_loss)
        obj_accuracy = [name, pair[1]]
        self.accuracy.append(obj_accuracy)
        return None
    # end definition add_pair()

    def get_average_accuracy(self) -> float:
        """
        Returns the average accuracy among the accuracies listed
        """
        avg_acc = 0
        for acc in self.accuracy:
            avg_acc = avg_acc + acc[1]
        return avg_acc/len(self.accuracy)
    # end of definition get_average_accuracy()

    def __str__(self) -> str:
        """
        Function to print the string representation of the object
        """
        obj_string = "\nModel: %s" % self.model_name
        obj_string = obj_string + "\nOptimizer stats: name = %s, epoch = %s, batch_size = %s, learning_rate = %s, momentum = %s" % \
            (self.optimizer_name,
             self.max_epoch,
             self.batch_size,
             self.learning_rate,
             self.momentum)
        obj_string = obj_string + "\nAccuracy: " + \
            str(self.accuracy) + "\nLoss: " + str(self.loss)
        return obj_string
# end class Statistics


class Statistics_Manager:
    """
    Description: This class provides functions for managing statistic objects

    Attributes
    ----------
    objects_list

    Functions
    ----------
    """
    objects_list = ()

    def __init__(self) -> None:
        """
        Constructor function
        """
        self.objects_list = ()
        return None
    # end of __init__()

    def add(self, object: Statistics_Object) -> None:
        """
        appends the statistics object to class list
        """
        new_list = list(self.objects_list)
        new_list.append(object)
        self.objects_list = tuple(new_list)
        return None
    # end of definition add()
    
    def print_by_accuracy(self) -> None:
        """
        prints all statistics objects in order by accuracy
        """
        sorted_list = []
        for current_obj in self.objects_list:
            if len(sorted_list) == 0: # check if there objects in list
                sorted_list.append(current_obj)
            else: # 
                index = 0
                while index < len(sorted_list): # inserting object in miidle of list
                    if current_obj.get_average_accuracy() > sorted_list[index].get_average_accuracy():
                        sorted_list.insert(index, current_obj)
                        break
                    else:
                        index = index +1
                # end of while
                if index == len(sorted_list): # if not inserted, appending to end of list
                    sorted_list.append(current_obj)
            # end of else
        # end of for
        for obj in sorted_list:
            print(obj)
        return None


    def print_by_attribute(self, attribute_name) -> None:
        """
        Prints all statistics object grouped by an attribute
        """
        unsorted_list = list(self.objects_list)
        sorted_list = []
        while len(unsorted_list) > 0:
            current_obj = unsorted_list[0]
            for compare_obj in unsorted_list:
                if getattr(compare_obj, attribute_name) == getattr(current_obj, attribute_name):
                    sorted_list.append(compare_obj)
                    unsorted_list.remove(compare_obj)
            # end for
        # end while
        for obj in sorted_list:
            print(obj)
        return None
    # end definition print_by_attribute

    def print(self) -> None:
        """
        Prints all statistics objects in list
        """
        for obj in self.objects_list:
            print(obj)

        return None
    # end of definition print
