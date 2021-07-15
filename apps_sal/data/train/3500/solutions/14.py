def remove_exclamation_marks(s):
    temp = list(s)
    while '!' in temp:
        temp.remove('!')
    return ''.join(temp)        
