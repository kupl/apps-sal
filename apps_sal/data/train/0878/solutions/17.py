for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    c = 0
    for i in range(n):
        sum += (a[i] - c - 1) // k
        c = a[i]
    print(sum)
