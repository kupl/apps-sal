def evil(n):
    return ["It's Odious!", "It's Evil!"][not str(bin(n)[2:]).count('1') % 2]
