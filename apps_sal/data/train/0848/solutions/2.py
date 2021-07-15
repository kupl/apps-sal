for i in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	arr_sum = []
	for i in range(len(arr)):
		arr_sum.append(arr[i]+arr[(i+1)%n]+arr[(i+2)%n])
	print(max(arr_sum))

