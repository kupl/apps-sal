s = 0
for m in range(int(input())):
	s = s + 1
	print(2*(sum(list(map(int, input().split())))-1))
