def evil(n):
    return "It's " + ('Evil!' if bin(n).count('1') % 2 == 0 else 'Odious!')
