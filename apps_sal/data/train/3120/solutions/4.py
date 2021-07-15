from typing import List, Union


def meeting(rooms: List[List[Union[str, int]]], number: int) -> Union[List[int], str]:
    chairs_in_rooms, chairs = (max(c - len(p), 0) for p, c in rooms), []

    while number > 0:
        try:
            n = next(chairs_in_rooms)
            chairs.append(min(n, number))
            number -= n
        except StopIteration:
            return "Not enough!"

    return chairs or "Game On"
