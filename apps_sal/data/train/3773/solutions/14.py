from typing import List


def isValid(f: List[int]):
    """ Check if choosen package of paterials is valid according to the rules. """
    return all(
        [
            (1 in f) ^ (2 in f) if 1 in f or 2 in f else True,
            (3 in f) ^ (4 in f) if 3 in f or 4 in f else True,
            all([5 in f, 6 in f]) if 5 in f or 6 in f else True,
            any([7 in f, 8 in f])
        ]
    )
