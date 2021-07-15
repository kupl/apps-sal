from math import inf
from itertools import chain, combinations, combinations_with_replacement

# thanks to "The capacity-C torch problem" by Roland Backhouse, Hai Truong
# https://www.sciencedirect.com/science/article/pii/S0167642315000118

def shortest_time(speed: [int]):
    forward_trips_num = 3       # for len(speed) == 4
    best_time = inf
#     path = []
    for forward_trips in combinations_with_replacement(list(combinations(speed, 2)), forward_trips_num):
        # not all people made at least one forward trip
        if any(list(chain(*forward_trips)).count(s) < speed.count(s) for s in set(speed)):
            continue
        sum_forward = sum([max(trip[0], trip[1]) for trip in forward_trips])     # time of all forward trips
        sum_return = 0                                                           # time of all return trips
        # number of return trips for each speed
        # (if there are several people with equal speed, the sum of all their return trips);
        returns = {s: 0 for s in set(speed)}
        for s in set(speed):
            # for every person the number of forward trips is one more than the number of return trips
            returns[s] += sum([trip.count(s) for trip in forward_trips]) - speed.count(s)
            sum_return += returns[s]*s

        if best_time > sum_forward+sum_return:
            best_time = sum_forward + sum_return
#             path = list(forward_trips) + list(chain(*[[(s,)]*returns[s] for s in set(speed)]))
#     print(path)
    return best_time
