import sys
input = sys.stdin.readline
from collections import deque

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
M = max(a)
a = deque(a)
cnt = 0
ans = [(-1, -1)]

while True:
    if a[0]==M:
        break
    
    A = a.popleft()
    B = a.popleft()
    ans.append((A, B))
    
    if A>B:
        a.appendleft(A)
        a.append(B)
    else:
        a.appendleft(B)
        a.append(A)
    
    cnt += 1

for _ in range(q):
    m = int(input())
    
    if m<=len(ans)-1:
        print(ans[m][0], ans[m][1])
    else:
        print(M, a[(m-cnt-1)%(n-1)+1])

