# n=int(input())
from bisect import bisect_right
# d=sorted(d,key=lambda x:(len(d[x]),-x))  d=dictionary     d={x:set() for x in arr}
# n=int(input())
#n,m,k= map(int, input().split())
import heapq
# for _ in range(int(input())):
#n,k=map(int, input().split())
# input=sys.stdin.buffer.readline
# for _ in range(int(input())):
n = int(input())
arr = list(map(int, input().split()))
ans = set()
s = set()
for i in range(n):
    s = {arr[i] | j for j in s}
    s.add(arr[i])
    ans.update(s)
    # print(s)
print(len(ans))
