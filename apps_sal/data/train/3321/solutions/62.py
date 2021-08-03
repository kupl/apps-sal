def evil(n):
    c = bin(n)
    if str(c).count("1") % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
