
def main2(n, x, l, q, ab):
    ary = [[0] * n for _ in range(30)]
    # ary[k][i]:ホテルiから2^k日かけてたどり着ける最も右のホテル
    idx = 1
    for i in range(n):
        while idx + 1 < n and x[idx + 1] - x[i] <= l:
            idx += 1
        ary[0][i] = idx
    for k in range(29):
        for i in range(n):
            if ary[k][i] < n:
                ary[k + 1][i] = ary[k][ary[k][i]]
            else:
                ary[k + 1][i] = n
    # a->bにかかる日数
    ret = []
    for a, b in ab:
        a, b = a - 1, b - 1
        if a > b:
            a, b = b, a
        tmp = 0
        k = 0
        while a < b:
            k = 0
            while ary[k + 1][a] < b:
                k += 1
            tmp += 1 << k
            a = ary[k][a]
        ret.append(tmp)
    return ret


def __starting_point():
    n = int(input())
    x = list(map(int, input().split()))
    l = int(input())
    q = int(input())
    ab = [list(map(int, input().split())) for _ in range(q)]
    ret2 = main2(n, x, l, q, ab)
    print(*ret2, sep='\n')


__starting_point()
