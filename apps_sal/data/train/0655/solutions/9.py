for _ in range(int(input())):
    n, k, v = map(int, input().split())
    a = [int(i) for i in input().split()]
    s = (n + k) * v - sum(a)
    if sum(a) >= (n + k) * v or s % k != 0:
        print(-1)
    else:
        print(s // k)
