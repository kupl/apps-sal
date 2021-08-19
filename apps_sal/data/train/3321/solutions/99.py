def evil(n):
    one_count = bin(n).count('1')
    if one_count % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
