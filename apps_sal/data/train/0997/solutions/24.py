import sys
def input(): return sys.stdin.readline().rstrip()


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = [10] * n
    for i in range(m):
        x, y, z = list(map(int, input().split()))
        for i in range(x - 1, y):
            a[i] *= z
    print(sum(a) // len(a))
