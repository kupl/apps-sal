def solve():
    n = int(input())
    b = list(map(int, input().split()))
    key = True
    for i in range(n - 2, -1, -1):
        if key and b[i] < b[i + 1]:
            key = False
        elif not key and b[i] > b[i + 1]:
            print(i + 1)
            return
    print(0)


for _ in range(int(input())):
    solve()

