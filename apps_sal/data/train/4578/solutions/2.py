import re
from itertools import chain
_VALUE = {'foul': -30, 'goal': 10, 'Snitch': 150}
_TEAMS = re.compile('(.+) vs (.+)')
_ACTION = re.compile('(.+): \\S+ (\\S+)')


def quidditch_scoreboard(teams, actions):
    scores = {team: 0 for team in _TEAMS.match(teams).groups()}
    for action in actions.split(', '):
        (team, event) = _ACTION.match(action).groups()
        scores[team] += _VALUE[event]
        if event == 'Snitch':
            break
    return '{}: {}, {}: {}'.format(*chain.from_iterable(list(scores.items())))
