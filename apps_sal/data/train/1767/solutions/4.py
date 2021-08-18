from collections import Counter


class SubCounter(Counter):
    def __le__(self, other):
        return all(value <= other[key] for key, value in self.items())


MELDS = [SubCounter({str(n): 3}) for n in range(1, 10)]
MELDS.extend([SubCounter([str(n), str(n + 1), str(n + 2)]) for n in range(1, 8)])


def solution(tiles):
    def remove(cnt):
        if sum(cnt.values()) == 4:
            for k, v in cnt.items():
                if v >= 2:
                    p = SubCounter(cnt)
                    p[k] -= 2
                    for m in MELDS:
                        if p <= m:
                            winning.update((m - p).keys())
        if sum(cnt.values()) == 1:
            winning.update(cnt.keys())
        else:
            for m in MELDS:
                if m <= cnt:
                    remove(cnt - m)
    winning, cnt = set(), SubCounter(tiles)
    forbidden = {k for k, v in cnt.items() if v >= 4}
    return remove(cnt) or ''.join(sorted(winning - forbidden))
