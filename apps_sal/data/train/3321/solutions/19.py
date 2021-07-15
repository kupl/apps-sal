def evil(n):
    return "It's {}!".format(('Evil', 'Odious')[f'{n:b}'.count('1') % 2])
