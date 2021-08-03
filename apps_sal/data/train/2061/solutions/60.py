import sys
from math import floor
def input(): return sys.stdin.readline().strip()


def sub(ax, ay, bx, by, cx, cy):
    mx, my = (ax + bx + cx) / 3, (ay + by + cy) / 3
    mx, my = floor(mx * 2), floor(my * 2)
    k = max(abs(mx), abs(my))
    if k == 0:
        return 0
    if k <= 1:
        return 1 if (mx, my) != (-1, -1) else 2
    return k if mx != my else k + 1


def main():
    T = int(input())
    ans_list = []
    """
    L字の重心を考えることで、L字を点として扱える。
    特に各マスを2x2に4等分することで、点の移動方法も明確に視覚化できる。
    """
    for _ in range(T):
        ax, ay, bx, by, cx, cy = list(map(int, input().split()))
        ans_list.append(sub(ax, ay, bx, by, cx, cy))
    for ans in ans_list:
        print(ans)


def __starting_point():
    main()


__starting_point()
