import numpy as np
for _ in range(int(input())):
	n,m = map(int,input().split())
	order = np.zeros((n*m,2),dtype=np.uint8)
	state = np.ones((n,m),dtype=np.uint8)*2
	for i in range(n):
		j = 0
		for e in map(int,input().split()):
			order[e-1] = i,j
			j+=1

	for i0 in range(n*m-1,-1,-1):
		i,j = order[i0]
		# print(i,j)
		if state[i,j]==2:#same as init or not changed till now
			# print(i,j)
			j_start = j_end = j
			state[i,j]=1#clean at the end
			while i<n-1:
				i+=1
				j_start = max(0,j_start-1)
				j_end = min(m,j_end+1)
				state[i,j_start:j_end+1] &= 1# if will be cleaned later not affected
				#if init or dirty marked as dirty set to 0
				# print(i,j_start,j_end)
	# print(order)
	for i in range(n):
		print(''.join(map(str,state[i])))
