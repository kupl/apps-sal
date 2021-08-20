def quidditch_scoreboard(teams, actions):
    t = teams.split(' vs ')
    D = {n: 0 for n in t}
    for a in actions.split(','):
        D[a[:a.find(':')].strip()] += [p for (w, p) in [('Snitch', 150), ('goal', 10), ('foul', -30)] if w in a].pop()
        if 'Snitch' in a:
            break
    return f'{t[0]}: {D[t[0]]}, {t[1]}: {D[t[1]]}'
