from math import ceil
from typing import Union


def calculate_tip(amount: int, rating: str) -> Union[int, str]:
    """ Calculates how much you need to tip based on the total amount of the bill and the service. """
    tips = {
        "terrible": 0,
        "poor": 5,
        "good": 10,
        "great": 15,
        "excellent": 20
    }
    tip = tips.get(rating.lower())
    if tip is None:
        return "Rating not recognised"
    return ceil(amount * (tip / 100))
