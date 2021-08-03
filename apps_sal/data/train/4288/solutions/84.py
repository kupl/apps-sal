import re


def quote(fighter):
    if re.match(r"George Saint Pierre", fighter, re.IGNORECASE):
        return "I am not impressed by your performance."
    if re.match(r"Conor McGregor", fighter, re.IGNORECASE):
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    pass
