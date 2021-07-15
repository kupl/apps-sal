# cook your dish here
n, m = map(int, input().split())
for i in range(m):
    q = int(input())
    if q < n + 2:
        print(0)
    else:
        s = 3 * n - q
        if s < n:
            print(s + 1)
        else:
            print(q - (2 + n) + 1)

