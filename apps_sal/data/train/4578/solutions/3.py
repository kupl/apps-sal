def quidditch_scoreboard(teams, actions):
    (t1, t2) = teams.split(' vs ')
    D = {t1: 0, t2: 0}
    for action in actions.split(', '):
        (t, a) = action.split(': ')
        if a.endswith('goal'):
            D[t] += 10
        elif a.endswith('foul'):
            D[t] -= 30
        else:
            D[t] += 150
            break
    return ', '.join((f'{k}: {v}' for (k, v) in D.items()))
