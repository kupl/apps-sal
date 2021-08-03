from sys import intern


def calc(cards, i=1, memo={}):
    if len(cards) == 1:
        memo[intern(str((i, cards)))] = cards[0] * 2**i
        return cards[0] * 2**i

    if str((i, cards)) in memo:
        return memo[intern(str((i, cards)))]

    result = max(cards[0] * 2**i + calc(cards[1:], i + 1, memo),
                 cards[-1] * 2**i + calc(cards[:-1], i + 1, memo))
    memo[intern(str((i, cards)))] = result

    return result
