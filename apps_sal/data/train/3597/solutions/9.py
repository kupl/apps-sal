from typing import List


def say_hello(name: List[str], city: str, state: str) -> str:
    """ Prepare a greeting based on input data. """
    return 'Hello, {n}! Welcome to {c}, {s}!'.format(n=' '.join(name), c=city, s=state)
