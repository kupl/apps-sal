# cook your dish here
n, m = map(int, input().split())

for _ in range(m):
    q = int(input())

    if q - n - 1 > n:
        print(3 * n - q + 1)

    elif q < n + 2 or q > (3 * n):
        print(0)

    else:
        print(q - n - 1)
