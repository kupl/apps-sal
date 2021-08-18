import sys


def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    for _ in range(II()):
        h, w = MI()
        cc = [list(map(int, list(SI()))) for _ in range(h)]
        ss = [SI() for _ in range(h)]
        aa = [[0] * w for _ in range(h)]
        mm = [[0] * w for _ in range(h)]
        cyc = [0]
        ci = 1
        dir = "UDLR"
        dij = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for si in range(h):
            for sj in range(w):
                if aa[si][sj] != 0:
                    continue
                i, j = si, sj
                d = -1
                stack = []
                while aa[i][j] == 0:
                    aa[i][j] = d
                    stack.append((i, j))
                    d -= 1
                    di, dj = dij[dir.index(ss[i][j])]
                    i, j = i + di, j + dj
                if aa[i][j] > 0:
                    a = aa[i][j]
                    dist = cyc[a]
                    m = (mm[i][j] + 1) % dist
                    for i, j in stack[::-1]:
                        aa[i][j] = a
                        mm[i][j] = m
                        m = (m + 1) % dist
                else:
                    dist = aa[i][j] - d
                    cyc.append(dist)
                    m = 0
                    for i, j in stack[::-1]:
                        aa[i][j] = ci
                        mm[i][j] = m
                        m = (m + 1) % dist
                    ci += 1
        one = [set() for _ in range(ci)]
        for i in range(h):
            for j in range(w):
                if cc[i][j] == 0:
                    one[aa[i][j]].add(mm[i][j])
        ans1 = sum(cyc)
        ans2 = sum(min(ck, len(ok)) for ck, ok in zip(cyc, one))
        print(ans1, ans2)


main()
