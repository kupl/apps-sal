import math
t = eval(input())
for i in range(0,t):
	K = int(input())
	ans = []
	arr = [8,0,2,4,6]
	temp = 1
	i = 0
	while(temp > 0):
		k = arr[int(math.ceil(K/math.pow(5,i)))%5]
		i = i + 1
		temp = math.floor(float(K-1)/math.pow(5,i))
		ans.append(str(k))
	ans.reverse();
	print(''.join(ans))
