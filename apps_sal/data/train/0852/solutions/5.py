def solve(n):
    if n % 2 == 0:
        for i in range(1, n + 1):
            if i % 2:
                j = 0
            else:
                j = 1
            for k in range(1, n + 1):
                print(j, end='')
                if j == 1:
                    j = 0
                else:
                    j = 1
            print()
    else:
        j = 0
        for i in range(1, n + 1):
            for k in range(1, n + 1):
                print(j, end='')
                if j == 1:
                    j = 0
                else:
                    j = 1
            print()


for _ in range(int(input())):
    n = int(input())
    solve(n)
