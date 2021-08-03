import sys
max_int = 1000000001  # 10^9+1
min_int = -max_int

t = int(input())
for _t in range(t):
    n, m, a, b = list(map(int, sys.stdin.readline().split()))

    if n * a != m * b:
        print('NO')
        continue
    print('YES')

    pointer = -1
    for i in range(n):
        row = ['0'] * m
        for j in range(a):
            pointer = (pointer + 1) % m
            row[pointer] = '1'
        print(''.join(row))
