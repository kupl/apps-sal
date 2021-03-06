import math


def is_ccw_turn(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1]) > 0


'\nIteratively generate a hull by finding items with the maximum distance from the current hull, adding them, and repeating.\nCurrently very inefficient.\n'


def quickhull(points):

    def dist(a, b, c):
        A = b[1] - a[1]
        B = a[0] - b[0]
        C = a[1] * b[0] - a[0] * b[1]
        return abs(A * c[0] + B * c[1] + C)

    def triangle_area(a, b, c):
        return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])

    def quickhull_recurse(a, b, targets, indent=1):
        targets = [p for p in targets if dist(a, b, p) != 0]
        if len(targets) == 0:
            return []
        max_dist = max([dist(a, b, p) for p in targets])
        m = min([p for p in targets if dist(a, b, p) == max_dist])
        l_targets = quickhull_recurse(a, m, [p for p in targets if not is_ccw_turn(m, a, p)], indent + 1)
        r_targets = quickhull_recurse(m, b, [p for p in targets if not is_ccw_turn(b, m, p)], indent + 1)
        return l_targets + [m] + r_targets
    (least, most) = (min(points), max(points))
    points = [p for p in points if p != most and p != least]
    top = quickhull_recurse(least, most, [p for p in points if is_ccw_turn(least, most, p)])
    bot = quickhull_recurse(most, least, [p for p in points if not is_ccw_turn(least, most, p)])
    return [least] + top + [most] + bot


"\nGenerate a merged hull by splitting the hull arbitrarily, generating two parting hulls, and reconciling.\nFirst, remove all points in hull 2's inner edge, if the centroid of hull 1 is outside hull 2.\nThen, reconcile all points into a single queue, ordered by angle, then distance.\nFinally, run a graham scan on this new monotone ring.\nDOESN'T CURRENTLY RUN TOO WELL.\n"


def unsorted_merge_hull(points):
    if len(points) <= 5:
        return double_half_hull(points)
    else:
        (a, b) = (unsorted_merge_hull(points[:len(points) // 2]), unsorted_merge_hull(points[len(points) // 2:]))
        c = (sum([x for (x, y) in a[:3]]) / 3, sum([y for (x, y) in a[:3]]) / 3)
        i = 0
        while i < len(b) or is_ccw_turn(c, b[i], b[(i + 1) % len(b)]) or is_ccw_turn(c, b[i], b[(i - 1) % len(b)]):
            i += 1
        if i < len(b):
            j = 0
            while j < len(b) or is_ccw_turn(c, b[j], b[(j + 1) % len(b)]) or is_ccw_turn(c, b[j], b[(j - 1) % len(b)]):
                j += 1
            if i < j:
                b = b[i:j]
            else:
                b = b[j:] + b[:i]
        q = []
        (i_a, i_b) = (0, 0)
        while i_a < len(a) or i_b < len(b):
            pass
        if i_a < len(a):
            q.extend(a[i_a:])
        if i_b < len(b):
            q.extend(b[i_b:])


"\nGenerate a merged hull by splitting the hull along a single axis, generating a series of partial hulls, and merging.\nHas issues with colinear points, but that's fine. \nThe main benefit of this is the ability to parallel process. \nSo long as the final set of points is re-checked, you can still get great gains from this.\nSift 90%, then run a better algo on the final result.\n"


def x_laced_merge_hull(points):
    sorted_points = sorted(points)
    x_laced_points = []
    for p in sorted_points:
        x_laced_points.append(p)
        if len(x_laced_points) >= 3 and x_laced_points[-1][0] == x_laced_points[-2][0] == x_laced_points[-3][0]:
            x_laced_points.pop(-2)

    def sew(l_h, r_h, l_o, r_o, direction):
        (l_i, r_i) = (l_o, r_o)
        found_both = False
        while not found_both:
            found_both = True
            moving_right = True
            while moving_right:
                if direction == 'top':
                    m_res = is_ccw_turn(r_h[(r_i + 1) % len(r_h)], r_h[r_i], l_h[l_i])
                    p_res = is_ccw_turn(r_h[(r_i - 1) % len(r_h)], r_h[r_i], l_h[l_i])
                elif direction == 'bot':
                    m_res = is_ccw_turn(l_h[l_i], r_h[r_i], r_h[(r_i + 1) % len(r_h)])
                    p_res = is_ccw_turn(l_h[l_i], r_h[r_i], r_h[(r_i - 1) % len(r_h)])
                if m_res == p_res == False:
                    moving_right = False
                else:
                    r_i = (r_i + (1 if direction == 'top' else -1)) % len(r_h)
                    found_both = False
            moving_left = True
            while moving_left:
                if direction == 'top':
                    m_res = is_ccw_turn(r_h[r_i], l_h[l_i], l_h[(l_i + 1) % len(l_h)])
                    p_res = is_ccw_turn(r_h[r_i], l_h[l_i], l_h[(l_i - 1) % len(l_h)])
                elif direction == 'bot':
                    m_res = is_ccw_turn(l_h[(l_i + 1) % len(l_h)], l_h[l_i], r_h[r_i])
                    p_res = is_ccw_turn(l_h[(l_i - 1) % len(l_h)], l_h[l_i], r_h[r_i])
                if m_res == p_res == False:
                    moving_left = False
                else:
                    l_i = (l_i + (-1 if direction == 'top' else 1)) % len(l_h)
                    found_both = False
        return (l_i, r_i)

    def x_laced_recurse(l_i=0, r_i=len(x_laced_points)):
        if r_i - l_i <= 5:
            sub_points = x_laced_points[l_i:r_i]
            hull = double_half_hull(sub_points)
            return (hull.index(min(hull)), hull.index(max(hull)), hull)
        else:
            (l_min_i, l_max_i, l_h) = x_laced_recurse(l_i, (l_i + r_i) // 2)
            (r_min_i, r_max_i, r_h) = x_laced_recurse((l_i + r_i) // 2, r_i)
            (bot_i_l, bot_i_r) = sew(l_h, r_h, l_max_i, r_min_i, 'bot')
            (top_i_l, top_i_r) = sew(l_h, r_h, l_max_i, r_min_i, 'top')
            hull = []
            l_i = bot_i_l
            while l_i != top_i_l:
                hull.append(l_h[l_i])
                l_i = (l_i + 1) % len(l_h)
            hull.append(l_h[l_i])
            r_i = top_i_r
            while r_i != bot_i_r:
                hull.append(r_h[r_i])
                r_i = (r_i + 1) % len(r_h)
            hull.append(r_h[r_i])
            return (hull.index(min(hull)), hull.index(max(hull)), hull)
    return double_half_hull(x_laced_recurse()[2])


def graham_scan_hull(points):
    m = max([n[1] for n in points])
    o = min(points, key=lambda p: p[0] * m + p[1])
    points = sorted(points, key=lambda p: p[0] * m + p[1])
    points = sorted(points[1:], key=lambda p: math.atan2(p[0] - o[0], p[1] - o[1]))
    (h, points) = ([points[-1], o, points[0]], points[1:])
    for p in points:
        h.append(p)
        done = False
        while len(h) > 3 and (not is_ccw_turn(h[-1], h[-2], h[-3])):
            h.pop(-2)
    h = [[p[0], p[1]] for p in h[:-1]]
    return (h[2:] + h[:2])[::-1]


def double_half_hull(points):
    sorted_points = sorted(points)

    def half_hull(sorted_points):
        hull = []
        for p in sorted_points:
            while len(hull) > 1 and (not is_ccw_turn(hull[-2], hull[-1], p)):
                hull.pop()
            hull.append(p)
        hull.pop()
        return hull
    return half_hull(sorted_points) + half_hull(reversed(sorted_points))


def hull_method(points):
    points = [list(p) for p in set([tuple(p) for p in points])]
    print(points if len(points) < 80 else '{}...'.format(points[:80]), '\n')
    print('quickhull:')
    res_quickhull = quickhull(points)
    print(res_quickhull, '\n')
    print('x_laced_merge hull:')
    res_x_laced_merge_hull = x_laced_merge_hull(points)
    print(res_x_laced_merge_hull, '\n')
    print('graham_scan_hull:')
    res_graham_scan_hull = graham_scan_hull(points)
    print(res_graham_scan_hull, '\n')
    print('double_half_hull:')
    res_double_half_hull = double_half_hull(points)
    print(res_double_half_hull, '\n')
    hash_checkers = []
    for hull in [res_quickhull, res_x_laced_merge_hull, res_graham_scan_hull, res_double_half_hull]:
        hash_checkers.append({tuple(p) for p in hull})
    fail_to_matches = sum((hash_checkers[i] != hash_checkers[i + 1] for i in range(len(hash_checkers) - 1)))
    return [] if fail_to_matches > 0 else res_double_half_hull
