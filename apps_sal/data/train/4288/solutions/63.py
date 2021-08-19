ufc_fighters = {'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!", 'george saint pierre': 'I am not impressed by your performance.'}


def quote(fighter):
    return ufc_fighters.get(fighter.lower())
