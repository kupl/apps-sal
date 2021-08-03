def monty_hall(correct_door_number, participant_guesses):
    winners = 0
    for x in participant_guesses:
        if x != correct_door_number:
            winners += 1
    return(round((winners / len(participant_guesses)) * 100))
