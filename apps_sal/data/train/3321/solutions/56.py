def evil(n):
    return ["It's Evil!", "It's Odious!"][f'{n:b}'.count('1') % 2]
