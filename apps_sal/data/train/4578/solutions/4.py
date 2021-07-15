from collections import Counter

def quidditch_scoreboard(teams, actions):
    ts = teams.split(' vs ')
    scores = dict.fromkeys(ts, 0)
    for action in actions.split(', '):
        team, a = action.split(': ')
        if a == 'Caught Snitch':
            scores[team] += 150
            break
        elif a == 'Quaffle goal':
            scores[team] += 10
        elif a.endswith('foul'):
            scores[team] -= 30
    return ', '.join(f'{team}: {scores[team]}' for team in ts)
