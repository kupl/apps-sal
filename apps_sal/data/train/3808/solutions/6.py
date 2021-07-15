def knight_or_knave(said):
    if said==True:
        return 'Knight!'
    elif said==False:
        return 'Knave! Do not trust.'
    elif eval(said)==True:
        return 'Knight!'
    return 'Knave! Do not trust.'
