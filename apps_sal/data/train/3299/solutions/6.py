from functools import lru_cache as memo


def calc(cards):

    @memo(None)
    def get_value(i, j, n):
        if i == j:
            return cards[i] * 2 ** n
        return max(cards[i] * 2 ** n + get_value(i + 1, j, n + 1), cards[j] * 2 ** n + get_value(i, j - 1, n + 1))
    return get_value(0, len(cards) - 1, 1)
