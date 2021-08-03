# cook your dish here
t = int(input())
for _ in range(t):
    n, k, v = list(map(int, input().split()))
    arr = list(map(int, input().split()))[:n]
    sums = sum(arr)
    l = v * (n + k)
    a = (l - sums) // k
    if(a <= 0):
        print(-1)
    elif((l - sums) % k != 0):
        print(-1)
    else:
        print(a)
