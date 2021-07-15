def invert(lst):
    invert = []
    
    for num in lst:
        if num < 0:
            invert.append(num - num - num)
        if num > 0:
            invert.append(num - num - num)
        if num == 0:
            invert.append(num)
    return invert
