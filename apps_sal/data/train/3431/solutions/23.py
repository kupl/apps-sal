from typing import List


def warn_the_sheep(queue: List[str]) -> str:
    """ Warn the sheep in front of the wolf that it is about to be eaten. """
    return "Pls go away and stop eating my sheep" if queue[-1] == "wolf" else f"Oi! Sheep number {list(reversed(queue)).index('wolf')}! You are about to be eaten by a wolf!"
