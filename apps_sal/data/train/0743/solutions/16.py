# cook your dish here
t = int(input())
for i in range(t):
    N, K = list(map(int, input().split()))
    rest = N / K
    if rest % K == 0:
        print("NO")
    else:
        print("YES")
