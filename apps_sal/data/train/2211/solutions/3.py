def solve():
    n, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] == d:
            print("1")
            return
    for i in range(n):
        if a[i] >= d:
            print("2")
            return
    print(int((d - 1) / (a[n - 1]) + 1))


for _ in range(int(input())):
    solve()
