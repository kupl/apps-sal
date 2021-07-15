t = int(input())
for _ in range(t):
    n=int(input())
    f = [int(i) for i in input().split()]
    r=max(f[0], f[-1])
    print(r)

