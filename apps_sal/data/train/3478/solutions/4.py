from itertools import zip_longest


def battle(player1, player2):
    result = {'player1': [], 'player2': []}
    for (creature1, creature2) in zip_longest(player1, player2, fillvalue=[0, 0]):
        if creature1[1] > creature2[0]:
            result['player1'].append(creature1)
        if creature2[1] > creature1[0]:
            result['player2'].append(creature2)
    return result
