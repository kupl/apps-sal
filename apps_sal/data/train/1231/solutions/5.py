import sys


def main():
    s = sys.stdin.readline
    t = int(s())
    for t in range(t):
        n = int(s())
        comp = str(2 ** n)
        sum = 0
        for i in comp:
            sum += int(i)
        print(sum)


def __starting_point():
    main()


__starting_point()
