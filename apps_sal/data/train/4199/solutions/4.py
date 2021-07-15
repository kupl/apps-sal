from typing import List

def squares(x: int, n: int) -> List[int]:
    """ Get an array of length `n`, starting with the given number `x` and the squares of the previous number. """
    result = [x]
    for _ in range(1, n):
        result.append(pow(result[-1], 2))
    return result if n > 0 else []
