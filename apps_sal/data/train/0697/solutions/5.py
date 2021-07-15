def maxSum(arr, n, k): 
	res = 0
	for i in range(k): 
		res += arr[i] 
	curr_sum = res 
	for i in range(k, n): 
		curr_sum += arr[i] - arr[i-k] 
		res = max(res, curr_sum) 
	return res 
for _ in range(int(input())):
    N, K = map(int, input().split(" "))
    lst = list(map(int, input().split(" ")))
    print(maxSum(lst, N, K))
