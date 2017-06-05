# Workout Log Sandbox to learn this stuff

class Exercise(object):
    'Super class of exercises that will include calisthenics, weights, and cardio.'

    def __init__(self, name, style, date, notes):
        self.name = name
        self.style = style
        self.date = date
        self.notes = notes


    def exerciseSummary(self):
        print("The %s is a %s exercise and was completed on %s!" %(self.name, self.style, self.date))

class Weighted(Exercise):
    'Weight sublcass includes exercises that required weight'

    def __init__(self, name, style, date, notes, reps, weight, sets):
        super().__init__(name, style, date, notes)
        self.reps = reps
        self.weight = weight
        self.sets = sets


class Calisthenic(Exercise):
    "Calisthenic sublcass includes exercises that don't require weight and aren't cardio"
    
    def __init__(self, name, style, date, notes, reps, sets):
        super().__init__(name, style, date, notes)
        self.reps = reps
        self.sets = sets

class Cardio(Exercise):
    "Cardio sublcass includes exercises that get the body moving"
    
    def __init__(self, name, style, date, notes, duration, distance):
        super().__init__(name, style, date, notes)
        self.duration = duration
        self.distance = distance

def Main():
    KnownExercises = [Calisthenic('Pushup', "Calisthenic", "June 5", "Got swole", "25", "5"),
                      Weighted("Bench Press", "Weighted", "June 4","get big", "5", "135", "3")
                      ]

    for exercise in KnownExercises:
        print("Name:" +exercise.name+ ", style:"+exercise.style)
        Exercise.exerciseSummary(exercise)

if __name__ == '__main__':
    Main()
