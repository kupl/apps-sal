from typing import List, Union


def find_spaceship(astromap: str) -> Union[List[int], str]:
    return next(([x, y] for y, r in enumerate(reversed(astromap.splitlines())) for x, c in enumerate(r) if c == 'X'),
                "Spaceship lost forever.")

