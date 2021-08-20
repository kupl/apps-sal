from sys import stdin


def main():
    n = int(stdin.readline())
    ls = [int(x) for x in stdin.readline().split()]
    ls = sorted(ls, reverse=True)
    s = 0
    for i in range(0, n, 2):
        s += ls[i]
    print(s)


def __starting_point():
    for _ in range(int(stdin.readline())):
        main()


__starting_point()
