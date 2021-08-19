from collections import deque


def solve(arr):
    flip = {'Left': 'Right', 'Right': 'Left'}
    directions = deque([flip.get(s, s) for s in [s.split()[0] for s in arr]])
    directions.reverse()
    directions.rotate(1)
    streets = [' '.join(s.split()[1:]) for s in arr][::-1]
    return [f'{direction} {street}' for (direction, street) in zip(directions, streets)]
