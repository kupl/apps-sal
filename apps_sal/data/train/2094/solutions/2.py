import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    x = s.count('z')
    y = (n - 4 * x) // 3
    for i in range(y):
        print(1, end=' ')
    for i in range(x):
        print(0, end=' ')


def __starting_point():
    main()


__starting_point()
