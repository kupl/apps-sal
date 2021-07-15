import math
t = int(input())
while t > 0:
	k = input()
	if len(k) == 0: continue;

	n, k = k.split()
	n = int(n)
	k = int(k)

	
	if n == 0 and  k == 1 : 
		print("0")
		t-=1
		continue
	elif n == 0:
		print((k*(k-1))%1000000007)
		t-=1
		continue
	
	level = n + math.ceil((k + 1)/2)
	time = (level - 1)*(level - 2)

	if k%2 == 0 : time = time + n;
	else : time = time + 2*(level-1) - n;
	print(time%1000000007)
	t-=1
