def knight_or_knave(said):
    if isinstance(said, str):
        return 'Knight!' if eval(said) == True else 'Knave! Do not trust.'
    else:
        return 'Knight!' if bool(said) == True else 'Knave! Do not trust.'
