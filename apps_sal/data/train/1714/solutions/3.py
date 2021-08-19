import math


def hull_method(pointlist):
    workset = set(map(tuple, pointlist))
    basepoint = edge = max(workset)
    (hull, ray) = ([], 0)

    def seeker(p):
        (dx, dy) = (p[0] - edge[0], p[1] - edge[1])
        turn = (math.atan2(dy, dx) - ray) % (2 * math.pi)
        sqdistance = dx * dx + dy * dy
        return (turn, -sqdistance, p)
    while not hull or basepoint != edge:
        (turn, _, edge) = min(list(map(seeker, workset - {edge})))
        ray += turn
        hull += [edge]
    return list(map(list, hull))
