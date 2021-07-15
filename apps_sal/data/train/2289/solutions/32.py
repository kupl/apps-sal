import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    inf = 10 ** 7
    s = input()
    n = len(s)
    s += "".join(chr(i + 97) for i in range(26))
    # print(s)
    # 次をその文字にした時の「長さ、位置」
    size = [0] * 26
    pos = [n + i for i in range(26)]
    # 解答復元のための移動先
    nxt = [-1] * n
    # 後ろの文字から順に見る
    for i in range(n - 1, -1, -1):
        min_size = inf
        min_pos = -1
        # 次をどの文字にすれば短くなるか調べる
        # 同じ長さの時は辞書順優先
        for sz, p in zip(size, pos):
            if sz < min_size:
                min_size = sz
                min_pos = p
        code = ord(s[i]) - 97
        size[code] = min_size + 1
        pos[code] = i
        nxt[i] = min_pos
        # print(size)
        # print(pos)
        # print(nxt)
        # print()
    # 最短になる最初の文字を調べて、nxtの順にたどる
    min_size = inf
    min_pos = -1
    for sz, p in zip(size, pos):
        if sz < min_size:
            min_size = sz
            min_pos = p
    i = min_pos
    ans = s[i]
    while i < n:
        i = nxt[i]
        ans += s[i]
    print(ans)

main()

