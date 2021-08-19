def quote(fighter):
    """Oпределяем победиеля"""
    f1 = str(fighter.lower())
    if f1 == 'george saint pierre':
        return 'I am not impressed by your performance.'
    elif f1 == 'conor mcgregor':
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return 'XUY'
