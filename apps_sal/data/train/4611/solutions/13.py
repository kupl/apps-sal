from typing import Tuple, Union

def animals(heads: int, legs: int) -> Union[str, Tuple[int]]:
    """ Find out how many chickens and cows are in the farm. """
    chickens, cows = heads - (legs / 2 - heads), (legs / 2 - heads)
    return (chickens, cows) if not any(
        [chickens < 0,
         cows < 0,
         not chickens.is_integer(),
         not cows.is_integer()]
    ) else "No solutions"
