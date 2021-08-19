# cook your dish here
n, m = map(int, input().split())
for i in range(m):

    q = int(input())
    if q < n + 2 or q > 3 * n:
        print(0)
    else:
        print(n - (abs(q - ((2 * n) + 1))))
