from typing import List


def who_is_paying(name: str) -> List[str]:
    """ Get the full name of the neighbor and the truncated version of the name as an array. """
    return [name, name[:2]] if len(name) > 2 else [name[:2]]
