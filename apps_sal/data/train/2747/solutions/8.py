from itertools import combinations


def count_rect_triang(points):
    ans = 0
    for c in combinations(set(map(tuple, points)), 3):
        dist = [(p[0][0] - p[1][0])**2 + (p[0][1] - p[1][1])**2 for p in combinations(c, 2)]
        ans += sum(dist) == max(dist) * 2
    return ans
