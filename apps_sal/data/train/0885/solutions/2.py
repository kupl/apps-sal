from sys import stdin
n = int(stdin.readline())
for _ in range(n):
    n1 = int(stdin.readline())
    b = bin(n1)[2:]
    print(b.count('0'))
