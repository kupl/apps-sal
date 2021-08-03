from itertools import cycle
from typing import List


def encode(message: str, key: int) -> List[int]:
    return [ord(m) - 96 + k for m, k in zip(message, cycle(list(map(int, str(key)))))]
