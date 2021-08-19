def quote(fighter):
    n = ['Conor McGregor'.lower(), 'George Saint Pierre'.lower()]
    if fighter.lower() == n[0].lower():
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return 'I am not impressed by your performance.'


x = quote('Conor McGregor')
print(x)
