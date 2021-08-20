def readintarray():
    return [int(s) for s in input().strip().split(' ')]


def solve(x, y, k, n):
    if abs(y - x) % k != 0:
        return False
    z = abs(y - x) // k
    return z % 2 == 0


for _ in range(int(input())):
    (x, y, k, n) = readintarray()
    print('Yes' if solve(x, y, k, n) else 'No')
