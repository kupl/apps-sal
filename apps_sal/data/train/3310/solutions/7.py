from collections import defaultdict


def score_pole_vault(vaulter_list):
    scoreboard = defaultdict(list)
    for v in vaulter_list:
        score = 0
        fails = 0
        for (i, result) in enumerate(v['results'], 1):
            fails += result.count('X')
            if 'O' in result:
                score = i * 10 - result.count('X')
        scoreboard[-score, fails].append(v['name'])
    nWinners = 0
    places = ['3rd', '2nd', '1st']
    answer = {}
    for performance in sorted(scoreboard):
        place = places.pop()
        winnerList = sorted(scoreboard[performance])
        l = len(winnerList)
        winners = ', '.join(winnerList)
        if l > 1:
            winners += ' (jump-off)' if place == '1st' else ' (tie)'
        answer[place] = winners
        nWinners += l
        if nWinners >= 3:
            break
        if nWinners == len(places) == 2:
            places.pop()
    return answer
