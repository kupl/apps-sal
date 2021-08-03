VISITED = dict()


def calc(cards, idx=0):
    if idx == 0:
        VISITED.clear()

    if len(cards) == 0:
        return 0

    tpl = tuple(cards)
    m_value = VISITED.get(tpl, None)
    if m_value:
        return m_value

    res = max(cards[0] * (2 << idx) + calc(cards[1:], idx + 1), cards[-1] * (2 << idx) + calc(cards[:-1], idx + 1))
    VISITED[tpl] = res
    return res
