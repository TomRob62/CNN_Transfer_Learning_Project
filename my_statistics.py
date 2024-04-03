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
    
    def add_loss(self, loss: float, name:str = "None") -> None:
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

    def __str__(self) -> str:
        """
        Function to print the string representation of the object
        """
        obj_string = "Model: %s" % self.name 
        obj_string = obj_string + "\nOptimizer stats: name = %s, epoch = %s, batch_size = %s, \
                                    learning_rate = %s, momentum = %s" % (self.optimizer_name, 
                                                                          self.max_epoch, 
                                                                          self.batch_size, 
                                                                          self.learning_rate,
                                                                            self.momentum)
        obj_string = obj_string + "\n" + str(self.accuracy) + "\n" + str(self.loss)
        return obj_string
# end class Statistics