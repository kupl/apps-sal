def evil(n):
    bit = bin(n)
    if bit.count('1') % 2 == 0:
        return "It's Evil!"
    return "It's Odious!"
