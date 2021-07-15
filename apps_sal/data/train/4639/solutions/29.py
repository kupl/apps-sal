def power_of_two(x):
    binary = bin(x)
    bits = [ones for ones in binary[2:] if ones == '1']
    if len(bits) == 1:
        return True
    else:
        return False
