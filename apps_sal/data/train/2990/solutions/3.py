def monty_hall(correct_door_number, participant_guesses):
    return round(100 * sum(1 for x in participant_guesses if x != correct_door_number) / len(participant_guesses))
