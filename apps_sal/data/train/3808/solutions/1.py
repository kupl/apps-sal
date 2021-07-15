def knight_or_knave(said):
    try:
        return 'Knight!' if eval(said) else 'Knave! Do not trust.'
    except:
        return 'Knight!' if said else 'Knave! Do not trust.'
