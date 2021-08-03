from functools import reduce
from collections import deque


def count_find_num(primesL, limit):
    initial_product = reduce(lambda prod, x: prod * x, primesL, 1)
    if initial_product > limit:
        return []

    found_numbers = set()
    queue = deque([initial_product])

    while len(queue) > 0:
        item = queue.popleft()
        found_numbers.add(item)

        for p in primesL:
            prod = p * item

            if prod <= limit:
                queue.append(prod)

    return [len(found_numbers), max(found_numbers)]
