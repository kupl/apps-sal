# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    ma = max(l)
    mi = min(l)
    for i in range(n):
        y = max(ma - i, i - mi)
        print(y, end=" ")
    print()
