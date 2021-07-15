display_board=lambda a,n:' %s '%(' \n'+(4*n-1)*'-'+'\n ').join(map(' | '.join,zip(*[iter(a)]*n)))
