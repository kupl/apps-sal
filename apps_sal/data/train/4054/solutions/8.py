import operator
calculations = {'norm_kill': lambda x: x * 100, 'assist': lambda x: x * 50, 'damage': lambda x: x * 0.5, 'healing': lambda x: x * 1, 'streak': lambda x: 2 ** x, 'env_kill': lambda x: x * 500}


def scoring(array):
    leaderboard = {}
    for player in array:
        score = 0
        for (action, value) in player.items():
            if action in calculations:
                score += calculations[action](value)
        leaderboard[player['name']] = score
    return [name for (name, score) in sorted(leaderboard.items(), key=operator.itemgetter(1), reverse=True)]
