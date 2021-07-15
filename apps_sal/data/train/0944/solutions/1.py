from sys import stdin, stdout
from collections import defaultdict
input = stdin.readline
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr3 = list(1 if i%2 else 0 for i in arr)
	for i in range(1, n):
		arr3[i] += arr3[i-1]
	arr2 = [arr[0]]
	for i in range(1, n):
		arr2.append(arr2[-1]+arr[i])
	ans = 0
	d = defaultdict(list)
	for i in range(n):
		if d[arr[i]]==[]:
			d[arr[i]].append(i)
		else:
			cnt1 = arr3[i-1]-arr3[d[arr[i]][0]]
			if (arr[i]%2 and cnt1%2) or (arr[i]%2==0 and (i-1-d[arr[i]][0]-cnt1)%2==0) :
				ans = max(ans, arr2[i-1]-arr2[d[arr[i]][0]])
			d[arr[i]] = [i]
	print(ans)
