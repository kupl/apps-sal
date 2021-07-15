def position(alphabet):
    
    txt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    x = txt.lower().find(alphabet) + 1
    
    solution =  'Position of alphabet: {}'
    
    return solution.format(x)
