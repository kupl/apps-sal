from typing import List


def sorter(textbooks: List[str]):
    """ Sort textbooks by subjects. """
    return sorted(textbooks, key=str.lower)
