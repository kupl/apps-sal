def evil(n):
    return ["It's Evil!", "It's Odious!"][bin(n).count('1') & 1]
