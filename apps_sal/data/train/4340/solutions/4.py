from math import inf
from itertools import chain, combinations, combinations_with_replacement


def shortest_time(speed: [int]):
    forward_trips_num = 3
    best_time = inf
    for forward_trips in combinations_with_replacement(list(combinations(speed, 2)), forward_trips_num):
        if any(list(chain(*forward_trips)).count(s) < speed.count(s) for s in set(speed)):
            continue
        sum_forward = sum([max(trip[0], trip[1]) for trip in forward_trips])
        sum_return = 0
        returns = {s: 0 for s in set(speed)}
        for s in set(speed):
            returns[s] += sum([trip.count(s) for trip in forward_trips]) - speed.count(s)
            sum_return += returns[s] * s

        if best_time > sum_forward + sum_return:
            best_time = sum_forward + sum_return
    return best_time
