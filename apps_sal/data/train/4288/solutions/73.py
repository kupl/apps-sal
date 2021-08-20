def quote(fighter):
    a = 'I am not impressed by your performance.'
    b = "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    c = 'Conor McGregor'.lower()
    return f'{b}' if fighter.lower() == c else f'{a}'
