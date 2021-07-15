try:
	n=int(input())
	x=[*map(int, input().split())]
	y=[*map(int, input().split())]
	for i in y:
		d=x.count(i)-y.count(i)
		if d!=0:
			print(i)
			break
except: pass
