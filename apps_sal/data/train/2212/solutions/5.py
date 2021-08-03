from sys import*
input = stdin.readline
n, q = map(int, input().split())
for _ in range(q):
    i = int(input())
    while i % 2 == 0:
        i += n - i // 2
    print((i + 1) // 2)
