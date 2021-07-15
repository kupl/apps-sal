from typing import Union


def how_much_water(water: int, load: int, clothes: int) -> Union[float, str]:
    if clothes > load * 2:
        return "Too much clothes"
    
    if clothes < load:
        return "Not enough clothes"

    return round(water * 1.1 ** (clothes - load), 2)

