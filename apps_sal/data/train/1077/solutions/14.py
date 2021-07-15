import sys
t = int( input() )
while t > 0:
	n = int( input() )
	ins = []
	while n > 0:
		s = input()
		ins.append(s)
		n -= 1
	idx = len(ins) - 2
	if ins[idx + 1].startswith('Left'):
		print('Begin' + ins[idx + 1][4:])
	else:
		print('Begin' + ins[idx + 1][5:])
	
	while idx >= 0:
		if ins[idx + 1].startswith('Left'):
			if ins[idx].startswith('Left'):
				print('Right' + ins[idx][4:])
			else:
				print('Right' + ins[idx][5:])
		else:
			if ins[idx].startswith('Left'):
				print('Left' + ins[idx][4:])
			else:
				print('Left' + ins[idx][5:])
		idx -= 1
	print('')
	t -= 1

