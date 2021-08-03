from functools import lru_cache


def calc(cards): return get(tuple(cards))


get = lru_cache(None)(lambda seq, turn=1: max([2**turn * seq[0] + get(seq[1:], turn + 1), 2**turn * seq[-1] + get(seq[:-1], turn + 1)])
                      if seq else 0)
