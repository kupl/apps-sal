import sys


def joseph(k, n=6):
    if k == 0:
        k = 1
    x = 0
    for i in range(2, n + 1):
        x = (x + k) % i
    return x


FLAMES = ['FRIENDS', 'LOVE', 'ADORE', 'MARRIAGE', 'ENEMIES', 'SISTER']

nCase = int(sys.stdin.readline())
for _ in range(nCase):
    a = ''.join(sys.stdin.readline().split())
    b = ''.join(sys.stdin.readline().split())
    n = 0
    for ch in set(a + b):
        n += abs(a.count(ch) - b.count(ch))
    print(FLAMES[joseph(n)])
