from typing import List


def wheat_from_chaff(values: List[int]) -> List[int]:
    i, latest_neg = 0, len(values)

    while i < latest_neg:
        if values[i] > 0:
            try:
                latest_neg = next(j for j in range(latest_neg - 1, i, -1) if values[j] < 0)
            except StopIteration:
                break
            values[i], values[latest_neg] = values[latest_neg], values[i]
        i += 1
    return values

