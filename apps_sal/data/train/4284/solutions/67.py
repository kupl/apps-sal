from typing import List


def array_leaders(numbers: List[int]) -> List[int]:
    leaders, s = [], sum(numbers)
    for n in numbers:
        s -= n
        if n > s:
            leaders.append(n)

    return leaders

