def strange_coach(players):
    letters = [p[0] for p in players]
    res = set((l for l in letters if letters.count(l) > 4))
    return ''.join(sorted(res)) if res else 'forfeit'
