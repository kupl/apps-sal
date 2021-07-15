for _ in range(int(input())):
	s=input()
	cnt=[0,0,0,0]
	for i in s:
		if i=='L':
			cnt[0]+=1
		elif i=='R':
			cnt[1]+=1
		elif i=='U':
			cnt[2]+=1
		else:
			cnt[3]+=1
	x=min(cnt[0],cnt[1])
	y=min(cnt[2],cnt[3])
	if x==0:
		if y==0:
			print("0")
		else:
			print("2\nDU")
	elif y==0:
		print("2\nLR")
	else:
		print(2*(x+y))
		print("L"*x  + "D"*y + "R"*x + "U"*y)
