def quote(fighter):
    return "I am not impressed by your performance." * (len(fighter) > 15) + "I'd like to take this chance to apologize.. To absolutely NOBODY!" * (len(fighter) < 15)
