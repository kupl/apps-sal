from sys import stdin
try:
    for _ in range(int(stdin.readline())):
        n, k = map(int, stdin.readline().rstrip().split())
        if n % 2 == 0:
            candy = ((k + 2) * n) // 2
        elif n == 3:
            candy = (3 + 3 * k)
        else:
            candy = ((k + 2) * (n - 1)) // 2 + (2 * k + 1)
        print(candy)
except:
    pass
