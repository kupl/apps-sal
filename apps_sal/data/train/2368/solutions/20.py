import math
t = int(input())
for g in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    a = min(A)
    b = min(B)
    ans = 0
    for i in range(n):
        ans += max(A[i]-a,B[i]-b)
    print(ans)
