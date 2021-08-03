def quidditch_scoreboard(teams, actions):
    teams = {i: 0 for i in teams.split(' vs ')}
    for i in actions.split(', '):
        team, action = i.split(': ')
        if 'goal' in action:
            teams[team] += 10
        elif 'foul' in action:
            teams[team] -= 30
        elif 'Snitch' in action:
            teams[team] += 150
            break
    return ', '.join('{}: {}'.format(i, teams[i]) for i in teams)
