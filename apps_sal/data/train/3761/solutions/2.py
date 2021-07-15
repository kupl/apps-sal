def strange_coach(players):
    firsts = [player[0] for player in players]
    return "".join(sorted(c for c in set(firsts) if firsts.count(c) >= 5)) or "forfeit"
