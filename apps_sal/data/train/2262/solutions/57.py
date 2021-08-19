import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def main():
    h, w, n = MI()
    points = []
    cnt = 0
    # 2点とも周上にある組のみ残す
    # 原点（左上）から反時計回りに移動した距離と点の通し番号を記録
    for _ in range(n):
        i0, j0, i1, j1 = MI()
        if (0 < i0 < h and 0 < j0 < w) or (0 < i1 < h and 0 < j1 < w):
            continue
        for i, j in [(i0, j0), (i1, j1)]:
            if j == 0 or i == h:
                d = i + j
            else:
                d = 2 * (h + w) - i - j
            points.append([d, cnt])
        cnt += 1
    points.sort()
    first = [True] * cnt
    visited = []
    # ABABのように２つの区間がずれて重なっていたらNO
    # ABBAのように完全に含まれるのはセーフ
    for d, pi in points:
        if first[pi]:
            visited.append(pi)
            first[pi] = False
        else:
            last_pi = visited.pop()
            if pi != last_pi:
                print("NO")
                return
    print("YES")


main()
