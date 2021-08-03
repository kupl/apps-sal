# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n & 1:
        print(n // 2 * (k + 2) + 2 * k + 1)
    else:
        print(n // 2 * (k + 2))
