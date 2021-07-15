def power_of_two(x):
    return x if x < 2 else int(bin(x)[3:]) == 0 
