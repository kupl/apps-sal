def powers_of_two(n):  
    power = 2 
    doubler = [1] 
    while n > 0:
        doubler.append(power) 
        n -= 1 
        power *= 2 
    return doubler
