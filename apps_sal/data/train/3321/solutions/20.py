def evil(n):
    return bin(n).count("1") % 2 and "It's Odious!" or "It's Evil!"
