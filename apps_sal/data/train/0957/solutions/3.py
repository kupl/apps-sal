from sys import stdin

for _ in range(int(stdin.readline())):
 n = int(stdin.readline())
 arr = sorted(list(map(int,stdin.readline().split())))
 m = max(arr[1] - arr[0], arr[n-1]-arr[n-2])
 for i in range(1, n-1):
  m = max(m, min(arr[i]-arr[i-1], arr[i+1]-arr[i]))
 print(m)

