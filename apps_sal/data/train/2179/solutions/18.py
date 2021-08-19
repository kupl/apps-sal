import sys


def main():
    (a, b, c) = list(map(int, sys.stdin.readline().split()))
    n = int(sys.stdin.readline().rstrip())
    x = list(map(int, sys.stdin.readline().split()))
    result = sum((1 for i in range(n) if b + 1 <= x[i] <= c - 1))
    sys.stdout.write(str(result) + '\n')


main()
