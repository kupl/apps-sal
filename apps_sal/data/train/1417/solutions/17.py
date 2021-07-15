for _ in range(int(input())):
	n = int(input())
	arr = [int(x) for x in input().split()]
	res = [0]*8
	for i in range(8):
		res[i] = arr.count(i+1)
	print(min(res))
