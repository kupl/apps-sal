def evil(n):
    binary = bin(n)[2:]
    binary_string = str(binary)
    num_of_1s = binary_string.count('1')
    if num_of_1s % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
