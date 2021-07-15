def knight_or_knave(said):
    if type(said)==str: 
        said=eval(said)
    return ['Knave! Do not trust.', 'Knight!'][said]
