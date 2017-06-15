"""workout_log sandbox to learn python stuff"""



class Exercise(object):
    'Super class of exercises that will include calisthenics, weights, and cardio.'

    def __init__(self, name, date, notes):
        self.name = name
        self.style = self.__class__.__name__
        # Makes the exercises subclass it's style, essentially eliminating the need for a variable
        self.date = date
        self.notes = notes


    def exercise_summary(self):
        'Prints stuff about exercise'
        print("The %s is a %s exercise and was completed on %s!"%(self.name, self.style, self.date))

    def detailed_summary(self):
        'prints all attributes of a class instance'
        print(vars(self))


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

def gen_new_exercise():
    'Prompt user to generate new exercise'
    input_exercise = []
    print("Is the exercise Calisthenic, Weighted, or Cardio?")
    input_class = input(">")
    input_class = globals()[input_class]
    if input_class == Calisthenic:
        input_name = str(input("What would you like to call this exercise?"))
        input_date = str(input("On what day was the exercise completed?"))
        input_note = str(input("Would you like to add any notes about the exercise?"))
        input_reps = str(input("How many reps are in each set?"))
        input_sets = str(input("How many total sets should be completed?"))
        input_exercise = [input_class(input_name, input_date, input_note, input_reps, input_sets)]
    else:
        print("That's unknown to me")
    return input_exercise


def prompt_user_for_workout_details():
    'docpenises'
    known_exercises = [Calisthenic('Pushup', "June 5", "Got swole", "25", "5"),
                       Weighted("Bench Press", "June 4", "get big", "5", "135", "3"),
                       Cardio(
                           "Bicycling", "June 1", "Lance Armstrong has 1 ball",
                           "131 min", "31 mi")]

    input_exercise = gen_new_exercise()

    known_exercises += input_exercise

    for exercise in known_exercises:
        print("Name:" +exercise.name+ ", style:"+exercise.style)
        Exercise.exercise_summary(exercise)
        #print(vars(exercise))
        Exercise.detailed_summary(exercise)

if __name__ == '__main__':
    prompt_user_for_workout_details()
