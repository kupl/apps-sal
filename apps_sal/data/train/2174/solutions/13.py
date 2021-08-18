from bisect import bisect_right
import heapq
n = int(input())
arr = list(map(int, input().split()))
ans = set()
s = set()
for i in range(n):
    s = {arr[i] | j for j in s}
    s.add(arr[i])
    ans.update(s)
print(len(ans))
