t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(" " * (n - i - 1) + '*' * (2 * i + 1))
        print(" " * (n - i - 1) + '*' * (2 * i + 1))
