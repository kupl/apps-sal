def quote(fighter: str) -> str:
    """ Get the right statement depending on the winner! """
    statements = {'george saint pierre': 'I am not impressed by your performance.', 'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"}
    return statements.get(fighter.lower())
