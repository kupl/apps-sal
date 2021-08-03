def evil(n):
    if not bin(n)[2:].count('1') % 2:
        return "It's Evil!"
    else:
        return "It's Odious!"
