def evil(n):
    binary = bin(n)
    
    ones = 0
    
    for i in binary:
        if i == '1':
            ones = ones + 1
    
    if ones % 2 == 0:
        return "It's Evil!"
    
    return "It's Odious!"
