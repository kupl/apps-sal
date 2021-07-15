def evil(n):
    n = bin(n)[2:]

    return "It's Evil!" if n.count('1') % 2 == 0 else "It's Odious!"
