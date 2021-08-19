def update_score(score, trump, alone, tricks):
    done = tricks.count(trump)
    mul = 2 if done == 5 and alone else 1
    add = 1 if done in (3, 4) else 2
    winner = trump if done > 2 else 3 - trump
    return [pts + (add * mul if team == winner else 0) for (team, pts) in enumerate(score, 1)]
