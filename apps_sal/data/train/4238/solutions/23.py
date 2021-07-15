def squares_needed(grains):
    count = 0
    square = 1
    while square <= grains:
        count += 1
        square = square * 2    
    return count
        

