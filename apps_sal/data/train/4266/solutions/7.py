from itertools import starmap
from operator import mul

def min_dot(a, b):
    return sum(starmap(mul,zip(sorted(a),sorted(b,reverse=True))))
