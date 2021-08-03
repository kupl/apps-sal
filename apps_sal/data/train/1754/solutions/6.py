import itertools


def valid(schedule):
    golfers = set(golfer for day in schedule for group in day for golfer in group)
    days = ["".join(day) for day in schedule]
    groups = [set(group) for group in sum(schedule, [])]
    return (
        all(day.count(golfer) == 1 for day in days for golfer in golfers)
        and len(set(len(day) for day in schedule)) == 1
        and len(set(len(group) for group in groups)) == 1
        and all(sum(pair <= group for group in groups) <= 1 for pair in map(set, itertools.combinations(golfers, 2))))
