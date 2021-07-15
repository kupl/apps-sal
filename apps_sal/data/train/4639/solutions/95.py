def power_of_two(x):
    return False if x == 0 else bin(x)[2:].count('1') == 1

   

