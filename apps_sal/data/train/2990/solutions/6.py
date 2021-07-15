from statistics import mean

def monty_hall(correct_door_number, participant_guesses):
    return round(mean([100 if p != correct_door_number else 0 for p in participant_guesses]))
