def squares_needed(grains):
    total=0
    square=0
    while grains>total:
        
        square+=1
        total+=2**(square-1)
    return square
