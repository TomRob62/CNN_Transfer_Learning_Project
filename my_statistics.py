class My_Statistics:
    epoch = 0
    lr = 4
    name = ""
    momentum = 0

    training_acc = 0
    valid_acc = 0
    test_acc = 0

    training_loss = 0
    valid_loss = 0
    test_loss = 0
    def __init__(self, epoch, learning_rate, name, momentum):
        self.epoch = epoch
        self.lr = learning_rate
        self.name = name
        self.momentum = momentum
        return None

    def print_statistics(self) ->  None:
        """Prints statistics to console"""
        print("Statistics for %s Model with %s epoch, %s learning rate, %s momentum." % (self.name, self.epoch, self.lr, self.momentum))
        print("\nTraining Loss: %s\t\tTraining Accuracy: %s" % (self.training_loss, self.training_acc))
        print("\nValidation Loss: %s\t\tValidation Accuracy: %s" % (self.valid_loss, self.valid_acc))
        print("\nTesting Loss: %s\t\tTesting Accuracy: %s\n\n" % (self.test_loss, self.test_acc))
    # end definition print statistics
        
    def save_statistics(self) -> None:
        """Saves statistics to text file "Statistics.txt"""
        file = open("Statistics.txt", "a")
        file.write("Statistics for %s Model with %s epoch, %s learning rate, %s momentum." % (self.name, self.epoch, self.lr, self.momentum))
        file.write("\nTraining Loss: %s\t\tTraining Accuracy: %s" % (self.training_loss, self.training_acc))
        file.write("\nValidation Loss: %s\t\tValidation Accuracy: %s" % (self.valid_loss, self.valid_acc))
        file.write("\nTesting Loss: %s\t\tTesting Accuracy: %s\n\n" % (self.test_loss, self.test_acc))
    # end definition save_statistics
# end class Statistics