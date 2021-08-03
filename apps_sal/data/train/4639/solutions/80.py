def power_of_two(x):
    if x == 0:
        return False
    return bin(x)[3:].find('1') == -1
