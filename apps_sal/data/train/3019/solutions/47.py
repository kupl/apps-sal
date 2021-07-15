def str_count(strng, letter):
    strngL = list(strng)
    letterCount = 0 
    for i in range(len(strngL)): 
        if strngL[i] == letter: 
            letterCount += 1
    return letterCount
