def evil(n):
    b = format(n, 'b')
    if b.count('1') % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
