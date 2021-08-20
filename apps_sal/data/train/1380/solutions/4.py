from sys import stdin, stdout
n = int(stdin.readline())
for _ in range(n):
    n1 = int(stdin.readline())
    abd = n1 * (n1 - 1) // 2
    print(abd)
