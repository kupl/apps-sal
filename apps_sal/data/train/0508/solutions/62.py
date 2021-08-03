import heapq as hq
import sys

stdin = sys.stdin


def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, q = nm()
    tl = []
    ins = list()
    dlt = list()
    vv = [tuple(nm()) for _ in range(n)]
    tl = [(s - x, 1, x) for s, _, x in vv]
    tl.extend([(t - x, 0, x) for _, t, x in vv])
    ww = [ni() for _ in range(q)]
    tl.extend([(t, 2) for t in ww])
    tl.sort()

    for x in tl:
        if x[1] == 1:
            hq.heappush(ins, x[2])
        elif x[1] == 0:
            hq.heappush(dlt, x[2])
            while dlt and ins[0] == dlt[0]:
                hq.heappop(ins)
                hq.heappop(dlt)
        else:
            print(-1 if not ins else ins[0])


def __starting_point():
    main()


__starting_point()
