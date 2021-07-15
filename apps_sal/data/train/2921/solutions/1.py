from itertools import count, cycle, islice

BLOCKS = ["gold", "diamond", "emerald", "iron"]


def blocks_to_collect(level):
    result = dict.fromkeys(BLOCKS, 0)
    for block, n in zip(islice(cycle(BLOCKS), level), count(3, step=2)):
        result[block] += n ** 2
    return {**result, "total": sum(result.values())}
