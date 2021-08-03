from sys import stdin

T = int(stdin.readline().strip())
for x in range(T):
    N = int(stdin.readline().strip())
    if N % 2 != 0:
        print('NO')
    else:
        print('YES')
