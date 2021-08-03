def evil(n):
    n = str(bin(n)).count('1')
    return 'It\'s {}!'.format(['Odious', 'Evil'][n % 2 == 0])
