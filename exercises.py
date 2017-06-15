"""workout_log sandbox to learn python stuff"""

from Workout_Log import Weighted, Cardio, Calisthenic


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
