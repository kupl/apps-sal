import sys
sys.setrecursionlimit(2147483647)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    n = int(input())
    A = [None] * n
    B = [None] * n
    for i in range(n):
        (A[i], B[i]) = map(int, input().split())
    if A == B:
        print(0)
        return
    print(sum(A) - min((b for (a, b) in zip(A, B) if a > b)))


resolve()
