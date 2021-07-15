import re
score_dict = {'Quaffle goal' : 10, 'Caught Snitch' : 150}

def quidditch_scoreboard(teams, actions):
    actions = re.sub(r'Caught Snitch.+', 'Caught Snitch', actions)
    actions = [action.split(':') for action in actions.split(',')]
    actions = [[item.strip() for item in action] for action in actions]
    team_one, team_two = teams.split(' vs ')

    team_one_sum = sum([score_dict.get(a[1], -30) for a in actions if a[0] == team_one])
    team_two_sum = sum([score_dict.get(a[1], -30) for a in actions if a[0] == team_two])

    return f'{team_one}: {team_one_sum}, {team_two}: {team_two_sum}'
