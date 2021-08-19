def evil(n):
    return ["It's Evil!", "It's Odious!"][format(n, 'b').count('1') % 2]
