m = 10 ** 9 + 7
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    else:
        g = pow(2, n - 1, m) - 2
        print(g)
