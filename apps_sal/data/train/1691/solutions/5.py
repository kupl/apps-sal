import sys
##from random import randint
n, m, c = [int(i) for i in input().split()]
matrix = [[0] * (m + 1) for i in range(n + 1)]
cc = 1
nn = 1
mm = 1
for nn in range(1, n + 1):
    for mm in range(1, m + 1):
        if cc <= c:
            print("2", end=' ')
            print(nn, nn, mm, mm)
            sys.stdout.flush()
            matrix[nn][mm] = int(input())
            cc += 1
        else:
            break
    if cc > c:
        break
print("3")
sys.stdout.flush()
for nn in range(1, n + 1):
    for mm in range(1, m + 1):
        if matrix[nn][mm] < 1 or matrix[nn][mm] > 50:
            print("25", end=' ')
        else:
            print(matrix[nn][mm], end=' ')
    print()
