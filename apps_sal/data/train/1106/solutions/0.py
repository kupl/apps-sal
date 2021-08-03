'''Well I found the bug, but I don't understand why it was doing that. I mean, as
far as I can tell, it shouldn't be a bug!
Note to self: deleting from (supposedly) local lists through recursion is dangerous!'''


class Group(object):
    def __init__(self, size, start, end, value):
        self.size = size
        self.start = start
        self.end = end
        self.value = value

    def __lt__(self, other):
        return self.start < other.start

    def __str__(self):
        return "%i: %i->%i, $%i" % (self.size, self.start, self.end, self.value)


def hash(car, i):
    people = []
    for group in car:
        people.extend([group.end] * group.size)
    people.sort()
    return tuple(people + [i])


def optimize(groups, car, capacity, i):
    if i == len(groups):
        return 0

    newcar = []
    pos = groups[i].start
    for group in car:
        if group.end > pos:
            newcar.append(group)
        else:
            capacity += group.size

    state = hash(newcar, i)
    try:
        return memo[state]
    except:
        v = optimize(groups, newcar, capacity, i + 1)
        if groups[i].size <= capacity:
            w = optimize(groups, newcar + [groups[i]], capacity - groups[i].size, i + 1) + groups[i].value
        else:
            w = 0

        if v > w:
            ie[state] = -1
        elif v < w:
            ie[state] = 1
        else:
            ie[state] = 0

        ans = max(v, w)
        memo[state] = ans
        return ans


cases = int(input())
for case in range(cases):
    memo = {}
    ie = {}
    groups = []
    n, _, capacity = list(map(int, input().split()))

    for g in range(n):
        size, start, end, value = list(map(int, input().split()))
        groups.append(Group(size, start, end, value))
    groups.sort()
    print(optimize(groups, [], capacity, 0))
