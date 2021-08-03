# coding:UTF-8
import sys


def resultSur97(x):
    return x % (10 ** 9 + 7)


def __starting_point():
    # ------ 入力 ------#
    nl = list(map(int, input().split()))     # スペース区切り連続数字

    x = nl[0]
    sList = [input() for _ in range(x)]

    # ------ 処理 ------#
    sListSorted = sorted(sList)
    out = ""
    for s in sListSorted:
        out += s

    # ------ 出力 ------#
    print(("{}".format(out)))
    # if flg == 0:
    #     print("YES")
    # else:
    #     print("NO")


__starting_point()
