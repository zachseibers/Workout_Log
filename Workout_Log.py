# Workout Log Sandbox to learn this stuff

class Exercise(object):
    'Class of exercises that will include calisthenics, weights, and cardio.'

    def __init__(self, name, style):
        self.name = name
        self.style = style
        
    
    def exerciseSummary(self):
        print("The %s is a %s exercise!" % (self.name, self.style))


pushup = Exercise(name='Pushup', style="Calisthenic")

pushup.exerciseSummary()