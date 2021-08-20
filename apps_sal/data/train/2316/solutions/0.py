import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(a) for a in input().split()]
    X = [0] * 30
    for a in A:
        for i in range(30):
            if a & 1 << i:
                X[i] += 1
    for i in range(30)[::-1]:
        if X[i] % 2:
            if X[i] == 1:
                print('WIN')
            elif N % 2 == 0:
                print('WIN')
            elif X[i] % 4 == 1:
                print('WIN')
            else:
                print('LOSE')
            break
    else:
        print('DRAW')
