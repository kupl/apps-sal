try:
	n=int(input())
	x=[*list(map(int, input().split()))]
	y=[*list(map(int, input().split()))]
	for i in y:
		d=x.count(i)-y.count(i)
		if d!=0:
			print(i)
			break
except: pass

