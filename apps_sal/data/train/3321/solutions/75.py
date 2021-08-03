def evil(n):
    return "It's Odious!" if bin(n)[1:].count('1') % 2 == 1 else "It's Evil!"
