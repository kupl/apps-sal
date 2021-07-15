#In the Name of God
import math

x = input().split()
n = int(x[0])
arr = []
i = 1
while(i<len(x)):
	arr.append(float(x[i]))
	i += 1
	arr.append(int(x[i]))
	i += 1
i = 0

ans = []
while(i<len(arr)):
	x = arr[i]
	i += 1
	y = arr[i]
	y = 10**y
	i += 1
	ans.append(x*y)
for i in range(len(ans)):
	print("{:.2f}".format(ans[i]))

