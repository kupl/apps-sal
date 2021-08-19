import sys
from collections import namedtuple


def readline():
    return list(map(int, input().split()))


def readlines():
    for line in sys.stdin.readlines():
        yield list(map(int, line.split()))


class State(namedtuple('State', 'payload time floor')):

    def hook(self, pivot, a, b):
        (lo, up) = (min(pivot, a, self.floor), max(pivot, a, self.floor))
        return (tuple((x for x in self.payload if x < lo or up < x)) + (b,), self.time + abs(self.floor - pivot) + abs(pivot - a))

    def choices_to_take_next(self, a, b):
        floor = self.floor
        (payload, time) = self.hook(floor, a, b)
        if len(payload) < 5:
            yield (payload, time)
            if floor > a:
                pivots = (x for x in self.payload if x > floor)
            elif floor == a:
                pivots = ()
            else:
                pivots = (x for x in self.payload if x < floor)
        else:
            pivots = self.payload
        for pivot in pivots:
            yield self.hook(pivot, a, b)


def time_to_get_free(payload, floor):
    if payload:
        (lo, up) = (min(payload), max(payload))
        return abs(lo - up) + min(abs(floor - lo), abs(floor - up))
    else:
        return 0


def main():
    (n,) = readline()
    floor = 1
    positions = {(): 0}
    for (a, b) in readlines():
        max_acceptable_time = min(positions.values()) + 16 - abs(floor - a)
        new_positions = dict()
        for (payload, time) in list(positions.items()):
            state = State(payload, time, floor)
            for (npayload, ntime) in state.choices_to_take_next(a, b):
                if ntime <= max_acceptable_time:
                    npayload = tuple(sorted(npayload))
                    if new_positions.setdefault(npayload, ntime) > ntime:
                        new_positions[npayload] = ntime
        positions = new_positions
        floor = a
    return min((t + time_to_get_free(p, floor) for (p, t) in list(positions.items()))) + 2 * n


print(main())
