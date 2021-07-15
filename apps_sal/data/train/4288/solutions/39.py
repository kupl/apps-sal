def quote(fighter: str) -> str:
    george = "George Saint Pierre".casefold()
    conor = "Conor McGregor".casefold()
    fighter = fighter.casefold()
    if fighter == george:
        return "I am not impressed by your performance."
    elif fighter == conor:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return ""
