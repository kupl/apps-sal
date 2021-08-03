for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in range(n):
        if a[i] % 2 == 1:
            odd += 1
    even = n - odd
    print(even * odd)
