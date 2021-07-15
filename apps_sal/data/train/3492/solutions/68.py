def correct_polish_letters(st): 
    new = ''
    for x in st:
        if x == 'ą':
            new += 'a'
        elif x == 'ć':
            new += 'c'
        elif x == 'ę':
            new += 'e'
        elif x == 'ł':
            new += 'l'
        elif x == 'ń':
            new += 'n'   
        elif x == 'ó':
            new += 'o'   
        elif x == 'ś':
            new += 's' 
        elif x == 'ź':
            new += 'z'
        elif x == 'ż':
            new += 'z'   
        else:
            new += x
    return new

          
            

