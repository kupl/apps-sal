def quote(fighter):
    fighter = fighter.lower()
    quote = {
        "george saint pierre": "I am not impressed by your performance.",
        "conor mcgregor": "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    }
    return quote[fighter]
