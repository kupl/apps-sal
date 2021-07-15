def evil(n):
    return "It's {}!".format('Odious' if sum(map(int, bin(n)[2:])) % 2 else 'Evil')
