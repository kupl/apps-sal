for _ in range(int(input())):
	n,m = map(int,input().split())
	print('1'*m)
	prev  = tuple(map(int,input().split()))
	for i in range(1,n):
		s = ''
		now = tuple(map(int,input().split()))
		prev_ = []
		for j in range(m):
			temp = prev[j]
			if j+1<m and prev[j+1]>temp:
				temp = prev[j+1]
			if j>0 and prev[j-1]>temp:
				temp = prev[j-1]
			if temp<now[j]:
				s += '1'
				temp = now[j]
			else:
				s += '0'
			prev_.append(temp)
		prev = prev_
		print(s)

