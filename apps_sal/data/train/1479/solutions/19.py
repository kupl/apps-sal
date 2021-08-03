# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        n, m = list(map(int, input().split()))
        if n == 9 or n == 10 or n == 11:
            continue
        elif a[n - 1] < m:
            a[n - 1] = m
    print(sum(a))
