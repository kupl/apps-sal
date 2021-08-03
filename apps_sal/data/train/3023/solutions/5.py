from collections import namedtuple


def best_match(goals1, goals2):
    Match = namedtuple('Match', ['diff', 'scored', 'index'])
    temp = [Match(xy[0] - xy[1], xy[1], idx) for idx, xy in enumerate(zip(goals1, goals2))]
    best_diff = min([match.diff for match in temp])
    temp = [match for match in temp if match.diff == best_diff]
    return sorted(temp, key=lambda match: match.scored, reverse=True)[0].index
