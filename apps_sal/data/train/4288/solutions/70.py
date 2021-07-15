def quote(fighter):
    cm = "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    gsp = "I am not impressed by your performance."
    if fighter.lower() == "george saint pierre":
        return gsp
    elif fighter.lower() == "conor mcgregor":
        return cm
    else:
        pass
