from math import hypot
from itertools import combinations

def peaceful_yard(yard, min_distance):
    positions = [(yard.index(row), row.index(cat)) for row in yard if row.replace("-", "") for cat in row.replace("-", "")]
    return all(hypot(x1-x0, y1-y0) >= min_distance for ((x0, y0), (x1, y1)) in combinations(positions, 2))
