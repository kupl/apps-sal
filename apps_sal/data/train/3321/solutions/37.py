def evil(n):
    x = bin(n).count('1')
    test = 'Odious' if x % 2 else 'Evil'
    return "It's {}!".format(test)
