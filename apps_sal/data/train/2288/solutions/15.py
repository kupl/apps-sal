
import sys


def main1(x, k, rary, q, ta):
    aary = []
    tary = []
    for i, (t, a) in enumerate(ta):
        aary.append([a, i])
        tary.append([t, i])
    tary.sort(key=lambda x: x[0])
    aary.sort(key=lambda x: x[0])
    l, r = 0, x
    lt, rt = -1, -1
    tidx = 0
    nowt = 0
    nowu = 'A'
    da = 0
    ret = [-1] * q
    daary = {}
    rary.append(10**9 + 1)
    k += 1
    for i, ri in enumerate(rary):
        while tidx < q and tary[tidx][0] <= ri:
            t, j = tary[tidx]
            tidx += 1
            a = ta[j][1]
            if nowu == 'A':
                if l <= a <= r:
                    ret[j] = a + da - (t - nowt)
                elif a < l:
                    ret[j] = da - daary[lt] - (t - nowt)
                else:
                    ret[j] = x + da - daary[rt] - (t - nowt)
            else:
                if l <= a <= r:
                    ret[j] = a + da + (t - nowt)
                elif a < l:
                    ret[j] = da - daary[lt] + (t - nowt)
                else:
                    ret[j] = x + da - daary[rt] + (t - nowt)
            ret[j] = max(0, ret[j])
            ret[j] = min(x, ret[j])
        if nowu == 'A':
            dt = ri - nowt
            da -= dt
            if l < -da:
                l = -da
                lt = ri
            nowt = ri
            nowu = 'B'
        else:
            dt = ri - nowt
            da += dt
            if r > x - da:
                r = x - da
                rt = ri
            nowt = ri
            nowu = 'A'
        daary[nowt] = da
        if l >= r:
            if nowu == 'B':
                da = 0
            else:
                da = x
            for ii in range(i + 1, k):
                ri = rary[ii]
                while tidx < q and tary[tidx][0] <= ri:
                    t, j = tary[tidx]
                    tidx += 1
                    if nowu == 'A':
                        ret[j] = da - (t - nowt)
                    else:
                        ret[j] = da + (t - nowt)
                    ret[j] = max(0, ret[j])
                    ret[j] = min(x, ret[j])
                if nowu == 'A':
                    da -= ri - nowt
                    da = max(da, 0)
                    nowu = 'B'
                else:
                    da += ri - nowt
                    da = min(da, x)
                    nowu = 'A'
                nowt = ri
            break
    return ret


input = sys.stdin.readline


def __starting_point():
    x = int(input())
    k = int(input())
    r = list(map(int, input().split()))
    q = int(input())
    ta = [list(map(int, input().split())) for _ in range(q)]
    print(*main1(x, k, r, q, ta), sep='\n')


__starting_point()
