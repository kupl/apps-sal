from typing import List


def find_multiples(integer: int, limit: int) -> List[int]:
    """ Get a list of all multiples based on integer and limit. """
    return list(filter(lambda _it: not _it % integer, range(1, limit + 1)))
