# cook your dish here
for o in range(int(input())):
	n = int(input())
	a = list(map(int ,input().split()))
	dic = {}
	s = 0
	for i in a:
		dic[i] = dic.get(i,0) +1
	for i in dic.values():
		if i >=2:
			s = s+i
	print(s//4)
