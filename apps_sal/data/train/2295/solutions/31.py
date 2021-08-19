import sys


def input():
    return sys.stdin.readline().rstrip()


def trans(l_2d):
    return [list(x) for x in zip(*l_2d)]


def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    same = []
    abb = trans(ab)
    if abb[0] == abb[1]:
        print(0)
        return
    mins = 10 ** 10
    for aabb in ab:
        if aabb[0] > aabb[1]:
            mins = min(aabb[1], mins)
    print(sum(abb[0]) - mins)


def __starting_point():
    main()


__starting_point()
