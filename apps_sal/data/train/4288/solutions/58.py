def quote(fighter):
    dict_of_responses = {
    "George Saint Pierre": "I am not impressed by your performance.",
    "george saint pierre": "I am not impressed by your performance.",
    "Conor McGregor": "I'd like to take this chance to apologize.. To absolutely NOBODY!",
    "conor mcgregor": "I'd like to take this chance to apologize.. To absolutely NOBODY!",
    }
    return dict_of_responses[fighter]
