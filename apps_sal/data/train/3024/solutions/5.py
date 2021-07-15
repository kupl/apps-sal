def friend(x):
    '''
    x: list of strings/people
    returns: list of people with only 4 letters in their names
    '''
    return [n for n in x if len(n) == 4]
