import sys


def query(n, a):
    while a % 2 == 0:
        a += n - a // 2
    return a // 2 + 1


n, q = list(map(int, sys.stdin.readline().split()))
sys.stdout.write("\n".join(str(query(n, int(input()))) for _ in range(q)))
