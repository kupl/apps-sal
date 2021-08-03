from collections import deque


def solve(arr):
    flip = {'Left': 'Right', 'Right': 'Left'}

    # Build the prefixes
    directions = deque([
        flip.get(s, s)
        for s in [s.split()[0] for s in arr]
    ])
    directions.reverse()
    directions.rotate(1)

    # Get the rest of the directions
    streets = [' '.join(s.split()[1:]) for s in arr][::-1]

    # Zip and concatenate each pair
    return [f'{direction} {street}' for direction, street in zip(directions, streets)]
