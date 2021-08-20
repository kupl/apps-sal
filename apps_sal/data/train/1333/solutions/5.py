import math
import sys
sys.setrecursionlimit(10 ** 3)
'def fast_expo(n):\n    mod=10**9+7\n    if n==1:\n     return 2\n    x=(fast_expo(n//2)%mod)\n    if n%2==0:\n     return (x*x)%(10**9+7)\n    else:\n     return (x*x*2)%(10**9+7)'
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    p = 0
    c = 0
    flag = 0
    mod = 10 ** 9 + 7
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            flag = 1
            break
        p += list(bin(l[i] & l[i - 1])[2:]).count('1')
    if flag == 1:
        print(0)
        continue
    t_2 = pow(2, p, mod)
    print(t_2)
