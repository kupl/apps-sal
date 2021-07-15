from typing import List

def number(lines: List[str]) -> List[str]:
    """ Add a line number (starting at 1) to every element of the list. """
    return list(map(lambda _it: "{}: {}".format(*_it), enumerate(lines, start=1)))
