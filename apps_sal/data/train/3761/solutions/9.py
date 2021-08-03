from collections import Counter


def strange_coach(players):
    return "".join(k for k, v in Counter([p[0] for p in sorted(players)]).items() if v > 4) or "forfeit"
