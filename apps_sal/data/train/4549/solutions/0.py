from heapq import *


def lemming_battle(battlefield, green, blue):
    hg, hb = ([-v for v in lst] for lst in (green, blue))
    heapify(hg)
    heapify(hb)

    while hb and hg:
        tmp_b, tmp_g = [], []
        for _ in range(min(battlefield, len(hg), len(hb))):
            cmp = heappop(hg) - heappop(hb)
            if cmp < 0:
                tmp_g.append(cmp)
            elif cmp > 0:
                tmp_b.append(-cmp)
        for lem in tmp_b:
            heappush(hb, lem)
        for lem in tmp_g:
            heappush(hg, lem)

    winner, lst = ("Green", hg) if hg else ("Blue", hb)
    survivors = ' '.join(str(-v) for v in sorted(lst))

    return ("Green and Blue died" if not hg and not hb else
            f"{winner} wins: {survivors}")
