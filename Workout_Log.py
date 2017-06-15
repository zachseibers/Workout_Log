"""workout_log sandbox to learn python stuff"""

import exercises
from exercises import Calisthenic

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
                       exercises.Weighted("Bench Press", "June 4", "get big", "5", "135", "3"),
                       exercises.Cardio(
                           "Bicycling", "June 1", "Lance Armstrong has 1 ball",
                           "131 min", "31 mi")]

    input_exercise = gen_new_exercise()

    known_exercises += input_exercise

    for exercise in known_exercises:
        print("Name:" +exercise.name+ ", style:"+exercise.style)
        exercises.Exercise.exercise_summary(exercise)
        #print(vars(exercise))
        exercises.Exercise.detailed_summary(exercise)

    record_workout_to_file(known_exercises)

def record_workout_to_file(known_exercises):
    'Record known_exercisesto a text file'
    with open('knownexercises.txt', 'w') as exercisesfile:
        for ex in known_exercises:
            exercisesfile.write("Exercise:%s \n" %ex)


if __name__ == '__main__':
    prompt_user_for_workout_details()
    