from math import ceil
from functools import lru_cache
three_details = lru_cache(None)(lambda n: int(n == 3) if n <= 3 else three_details(ceil(n / 2)) + three_details(n // 2))
