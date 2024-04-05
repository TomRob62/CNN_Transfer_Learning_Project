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
    max_epoch = -1
    learning_rate = -1
    batch_size = -1
    momentum = -1
    optimizer_name = ""
    model_name = ""

    # variables for storing model results
    # example loss = [['training_loss', 1.0510], ['testing_loss', 0.510351], []'None', 15.0650165]]
    loss = []
    accuracy = []


    def __init__(self, epoch = -1, batch_size = -1, learning_rate = -1, momentum = -1, optimzer = "", model = "") -> None:
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
        obj_string = obj_string + " \nAccuracy: " + \
            str(self.accuracy) + " \nLoss: " + str(self.loss)
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
    __init__
    add()
        adds a statistics object to objects_list
    print_by_accuracy()
        prints all objects in list sorted by accuracy
    print_by_attribute()
        prints all objects in list sorted by object attribute
    write_file()
        writes all objects to text file
    read_file()
        reads all objects in text file to objects_list
    """
    objects_list = ()

    def __init__(self) -> None:
        """
        Constructor function
        """
        self.objects_list = ()
        return None
    # end of __init__()

    def add(self, obj: Statistics_Object) -> None:
        """
        appends the statistics object to class list
        """
        new_list = list(self.objects_list)
        new_list.append(obj)
        self.objects_list = tuple(new_list)
        return None
    # end of definition add()
    
    def print_by_accuracy(self, limit = -1) -> None:
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
        for obj in sorted_list[:limit]:
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

    def write_file(self, file_name: str) -> None:
        """
        Write all statistics to a txt file
        """
        file = open(file_name, "a")
        for obj in self.objects_list:
            file.write(str(obj))
        return None
    # end definition write_file

    def read_file(self, file_name: str) -> None:
        """
        Reads a text file and generates a list of statistics objects. Then reassigns
        object_list to newly generated list.

        Text file must be generated by write_file. Any modification could
        result in error.
        """
        file = open(file_name, "r")

        list_objects = []
        obj = Statistics_Object()
        for line in file.readlines():
            # creating new statistics object
            if line.__contains__("Model"):
                obj.model_name = line[5:]
            elif line.__contains__("stats"):
                line_split = line.split()
                obj.optimizer_name = line_split[line_split.index("name")+2]
                obj.max_epoch = line_split[line_split.index("epoch")+2]
                obj.batch_size = line_split[line_split.index("batch_size")+2]
                obj.learning_rate = line_split[line_split.index("learning_rate")+2]
                obj.momentum = line_split[line_split.index("momentum")+2]
            elif line.__contains__("Accuracy:"):
                obj.accuracy = Statistics_Manager.extract_result(line)
            elif line.__contains__("Loss:"):
                obj.loss = Statistics_Manager.extract_result(line)
                list_objects.append(obj)
                obj = Statistics_Object()
        self.objects_list = tuple(list_objects)
        return None
    # end definition read file()

    def extract_result(line: str) -> list:
        """
        Helper function to extract results from text file
        """
        result_list = []
        modified_line = ""
        # removing non essential chars
        for char in line:
            if not (char == "[" or char == "]" or char == "," or char == "'"):
                modified_line = modified_line + char
        # seperating by space
        words_in_line = modified_line.split(" ")
        my_list = []
        name = ""
        words_in_line.pop(0)
        # generating sub list e.g. ['name', result:float] 
        # and appending to main list
        for word in words_in_line:
            if Statistics_Manager.has_num(word):
                my_list.append(name)
                my_list.append(float(word))
                result_list.append(my_list.copy())
                my_list = []
                name = ""
            else:
                name = name + word

        return result_list
    # end definition extract_result()

    def has_num(word: str) -> bool:
        """
        Returns if a string contains a number
        """
        nums = "0123456789"
        for charact in nums:
            if word.__contains__(charact):
                return True
            
        return False
# end class Statistics_Manager
