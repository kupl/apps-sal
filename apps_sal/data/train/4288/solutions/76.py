def quote(fighter):
    s = ["I am not impressed by your performance.",
         "I'd like to take this chance to apologize.. To absolutely NOBODY!"]
    return s[0] if fighter[0].lower() == "g" else s[1]
