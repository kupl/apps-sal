def display_board(a, n): return ' %s ' % (' \n' + (4 * n - 1) * '-' + '\n ').join(map(' | '.join, zip(*[iter(a)] * n)))
