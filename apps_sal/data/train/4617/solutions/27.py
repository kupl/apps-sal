from typing import List


def powers_of_two(n: int) -> List[int]:
    value = 1
    accu = [value]
    for i in range(n):
        value <<= 1
        accu.append(value)
    return accu
