def quote(fighter):
    r = {'george saint pierre': 'I am not impressed by your performance.', 'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"}
    return r.get(fighter.lower())
