import bisect
from collections import deque
def comb(fruits):
    energy = 0
    fruits = deque(sorted(fruits))
    while len(fruits) > 1:
        e = fruits.popleft() + fruits.popleft()
        energy +=  e
        bisect.insort_left(fruits, e)
    return energy
