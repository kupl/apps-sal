for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    r = a[0] ^ a[1]
    for i in range(2, n):
        r = r ^ a[i]
    print(r)
