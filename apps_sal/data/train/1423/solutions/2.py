# cook your dish here
T = int(input())
for i in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))[:N]
    K = int(input())
    val = x[K - 1]
    y = sorted(x)
    z = y.index(val)
    print(z + 1)
