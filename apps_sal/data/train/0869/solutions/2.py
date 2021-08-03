import sys


def main():
    s = sys.stdin.readline
    a = s().strip()
    b = s().strip()
    if b in a:
        print("Y")
    else:
        print("N")


def __starting_point():
    main()


__starting_point()
