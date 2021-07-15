from operator import itemgetter
from typing import Dict


def total_licks(env: Dict[str, int]) -> str:
    t = max(list(env.items()), key=itemgetter(1), default=('', 0))
    return (f"It took {252 + sum(env.values())} licks to get to the tootsie roll center of a tootsie pop."
            f"{f' The toughest challenge was {t[0]}.' if t[1] > 0 else ''}")

