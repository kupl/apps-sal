def solve(n):
    j = 1
    for i in range(1, n + 1):
        for k in range(n):
            print(j, end='')
            j += 1
        print()


for _ in range(int(input())):
    n = int(input())
    solve(n)
