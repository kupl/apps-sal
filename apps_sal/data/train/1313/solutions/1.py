from math import gcd,sqrt

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]

    g = A[0]
    for i in range(1,N):
        g = gcd(g,A[i])

    f = g
    # print(g,'$')
    for i in range(2,int(sqrt(g))+1):
        if(g%i==0):
            f = i
            break
    if(g!=1):
        ans.append(f)
    else:
        ans.append(-1)

for i in ans:
    print(i)
