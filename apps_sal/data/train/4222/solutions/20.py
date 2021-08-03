from typing import List


def get_size(w: int, h: int, d: int) -> List[int]:
    """ Get the total surface area and volume of a box as an array: `[area, volume]`. """
    return [(2 * w * h) + (2 * w * d) + (2 * d * h), w * h * d]
