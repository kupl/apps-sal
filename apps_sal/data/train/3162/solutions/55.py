from typing import Union


def compare(s1: Union[str, None], s2: Union[str, None]) -> bool:

    def value(s: Union[str, None]):
        return sum(map(ord, s.upper())) if s and all((c.isalpha() for c in s)) else 0
    return value(s1) == value(s2)
