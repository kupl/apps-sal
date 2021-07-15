for l in reversed([int(input()) for _ in range(11)]):
	ans = abs(l)**.5 + (l**3)*5
	print('f({}) ='.format(l), ('{:0.2f}'.format(ans) if 400 >=ans else  'MAGNA NIMIS!'))

