def stringy(size):
    counter = 0 
    res = ""
    while counter < size:
        if counter % 2 == 0:
            res += "1"
            counter += 1
        elif counter % 2 == 1:
            res += "0"
            counter += 1
    return res
