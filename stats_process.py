
import re
class Trial:
    loss = 0
    accuracy = 0
    name = ""
    def __init__(self):
        self.loss = []
        self.name = ""
        self.accuracy = []
        return None
    # end definition init

    def __str__(self) -> str:
        obj_string = "\n%s\nLoss: %s\nAccuracy: %s" % (self.name, self.loss, self.accuracy)
        return obj_string
    
    def average(self):
        self.loss = sum(self.loss)/3
        self.accuracy = sum(self.accuracy)/3
# end class trial   

trial_list = []
current_trial = Trial()
doc = open("Statistics.txt", "r")
for line in doc:
    if line == "":
        continue
    if line.__contains__("Statistics"):
        current_trial.average()
        trial_list.append(current_trial)
        current_trial = Trial()
        current_trial.name = line
    if line.__contains__("Loss"):
        components = re.split(" |\t", line)
        for num, comp in enumerate(components):
            if comp.__contains__("Loss"):
                current_trial.loss.append(float(components[num+1]))
            if comp.__contains__("Accuracy"):
                current_trial.accuracy.append(float(components[num+1]))

second_best = 0
best_index = 0
for num, obj in enumerate(trial_list):
    if obj.accuracy > trial_list[best_index].accuracy:
        second_best = best_index
        best_index = num
    elif obj.accuracy == trial_list[best_index].accuracy:
        if obj.loss < trial_list[best_index].loss:
            second_best = best_index
            best_index = num

print("Best: ")
print(trial_list[best_index])
print("\nSecond Best: ")
print(trial_list[second_best])
