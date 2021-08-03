import sys


def solve(n, k, a):
    for i in range(k):
        max_a = max(a)
        for i in range(len(a)):
            a[i] = max_a - a[i]
    print(' '.join([str(x) for x in a]))


def main():
    parts = sys.stdin.readline().strip().split(' ')
    n = int(parts[0])
    k = int(parts[1])
    if k > 2:
        k %= 2
        if k == 0:
            k = 2
    a = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    solve(n, k, a)


main()
