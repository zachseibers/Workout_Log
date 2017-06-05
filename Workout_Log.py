### Workout_Log Sandbox to learn this stuff
### 1 - How to build new exercise class based on user input, will need to write a function
### 2 - How do I store the known exercises to a text file or database
### 3 - During exercise generation, can I check to see if it already exists.
###     >If it does, prompt user to select existing and use it as a template.
### 4 - How to store a log of exercises
### 5 - Is my class structure correct, if recorded workouts are only particular insances, 
###     then I may need to generate classes for each activity, ie running is a subclass of cardo


class Exercise(object):
    'Super class of exercises that will include calisthenics, weights, and cardio.'

    def __init__(self, name, date, notes):
        self.name = name
        self.style = self.__class__.__name__   # Makes the exercises subclass it's style, essentially eliminating the need for a variable 
        self.date = date
        self.notes = notes


    def exerciseSummary(self):
        print("The %s is a %s exercise and was completed on %s!" %(self.name, self.style, self.date))
   
    def detailedsummary(self):
            print(vars(self))         #prints all attributes of a class instance


class Weighted(Exercise):
    'Weight sublcass includes exercises that required weight'

    def __init__(self, name, date, notes, reps, weight, sets):
        super().__init__(name, date, notes)
        self.reps = reps
        self.weight = weight
        self.sets = sets


class Calisthenic(Exercise):
    "Calisthenic sublcass includes exercises that don't require weight and aren't cardio"
    
    def __init__(self, name, date, notes, reps, sets):
        super().__init__(name, date, notes)
        self.reps = reps
        self.sets = sets

class Cardio(Exercise):
    "Cardio sublcass includes exercises that get the body moving"
    
    def __init__(self, name, date, notes, duration, distance):
        super().__init__(name, date, notes)
        self.duration = duration
        self.distance = distance

#def genNewExercise():
#     'Prompt user to generate new exercise'
#     input_Exercise = []
#     print("Is the exercise Calisthenic, Weighted, or Cardio?")
#     input_class = input(">")
#     if input_class == "Calisthenic":
#         input_name = str(input("What would you like to call this exercise?"))
#         input_date = str(input("On what day was the exercise completed?"))
#         input_note = str(input("Would you like to add any notes about the exercise?"))
#         input_reps = str(input("How many reps are in each set?"))
#         input_sets = str(input("How many total sets should be completed?"))
#     else:
#         print("That's unknown to me")
#     input_Exercise = [input_class(input_name, input_date, input_note, input_reps, input_sets)]
   

def Main():
    
    KnownExercises = [Calisthenic('Pushup', "June 5", "Got swole", "25", "5"),
                      Weighted("Bench Press", "June 4","get big", "5", "135", "3"),
                      Cardio("Bicycling", "June 1", "Lance Armstrong has 1 ball", "131 min", "31 mi")]
    
   # genNewExercise()
   # KnownExercises += input_Exercise

    for exercise in KnownExercises:
        print("Name:" +exercise.name+ ", style:"+exercise.style)
        Exercise.exerciseSummary(exercise)
        #print(vars(exercise))
        Exercise.detailedsummary(exercise)

if __name__ == '__main__':
    Main()
