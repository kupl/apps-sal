c = 0
n, s = list(map(int, input().split()))
arr = sorted([int(i) for i in input().split()])
if arr[n//2] < s:
   for i in range(n//2, n): c += (s - arr[i])*(arr[i] < s)
else:
   for i in range(n//2+1): c -= (s - arr[i])*(arr[i] > s)
print(c)

