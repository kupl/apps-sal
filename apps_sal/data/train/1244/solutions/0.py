c=0
for i in range (int(input ())):
	a, b=map(int, input().split())
	c+=abs(a-b)+1
print(c%((10**9) +7)) 
