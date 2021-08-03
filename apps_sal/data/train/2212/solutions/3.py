import sys


def query(n, a):
    while not (a & 1):
        a += (n - a // 2)
    return a + 1 >> 1


n, q = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(q)]
sys.stdout.write("\n".join(str(query(n, a)) for a in arr))
