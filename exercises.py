"""workout_log sandbox to learn python stuff"""


class Exercise(object):
    'Super class of exercises that will include calisthenics, weights, and cardio.'

    def __init__(self, name, date, notes):
        self.name = name
        self.style = self.__class__.__name__
        # Makes the exercises subclass it's style, essentially eliminating the need for a variable
        self.date = date
        self.notes = notes

    def __str__(self):
        return str(vars(self))

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

class BenchPress(Weighted):
    'Bench Press class so that individual exercises are recorded as objects'
    def __init__(self, name, date, notes, reps, weight, sets):
        super().__init__(self, name, date, notes, reps, weight, sets)


class Bicycling(Cardio):
    'Example Bicycling class so bike rides can be recorded'
    def __init__(self, name, date, notes, duration, distance):
        super().__init__(name, date, notes, duration, distance)

class Pushup(Calisthenic):
    'Basic Pushup'
    def __init__(self, name, date, notes, reps, sets):
        super().__init__(name, date, notes, reps, sets)
