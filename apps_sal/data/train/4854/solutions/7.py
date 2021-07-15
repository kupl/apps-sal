from __future__ import division
from numpy import *

def find_circle(a, b, c):
    if any(map(array_equal, (a, b, c), (b, c, a))): return
    (ax, ay), (bx, by), (cx, cy) = a, b, c
    d = ax * (by - cy) + bx * (cy - ay) + cx * (ay - by) << 1
    if not d: return
    t1, t2, t3 = (ax**2 + ay**2), (bx**2 + by**2), (cx**2 + cy**2)
    x = (t1*(by - cy) + t2*(cy - ay) + t3*(ay - by)) / d
    y = (t1*(cx - bx) + t2*(ax - cx) + t3*(bx - ax)) / d
    ab, bc, ca = linalg.norm(a - b), linalg.norm(b - c), linalg.norm(c - a)
    return x, y, ab*bc*ca / abs(d)

def count_circles(list_of_circles, point):
    (px, py), result = point, 0
    for circle in list_of_circles:
        if point in circle:
            result += 1
        else:
            res = find_circle(*map(array, circle))
            result += res and (px - res[0])**2 + (py - res[1])**2 <= res[2]**2
    return result
