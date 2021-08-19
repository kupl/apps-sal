import math


def crosstable(players, results):
    scores = {}
    places = []
    for (s, p) in zip(results, players):
        scores[p] = [sum((y for y in s if y != None))]
    c = 0
    for (x, p) in zip(results, players):
        scores[p].append(0)
        for (y, p_2) in zip(x, players):
            if y != None:
                scores[p][1] += scores[p_2][0] * y
        scores[p].append(c)
        c += 1
    del c
    for (x, y) in zip(scores.keys(), scores.values()):
        for (c, z) in enumerate(places):
            if z[0]['score'][0] < y[0] or (z[0]['score'][0] == y[0] and z[0]['score'][1] < y[1]):
                places.insert(c, [{'Player': x, 'score': y}])
                break
            elif z[0]['score'][0] == y[0] and z[0]['score'][1] == y[1]:
                places[c].append({'Player': x, 'score': y})
                break
        else:
            places.append([{'Player': x, 'score': y}])
    for (c, x) in enumerate(places):
        if len(x) > 1:
            places[c] = sorted((y for y in x), key=lambda a: a['Player'].split(' ')[1])
    cur_line = 0
    display_place = True
    longest_name = max((len(x) for x in players)) + 2
    longest_score = max((len('{:0.1f}'.format(x[0])) for x in scores.values()))
    longest_SB = max((len('{:0.2f}'.format(x[1])) for x in scores.values()))
    longest_rank = len(str(len(players) - len(places[-1]) + 1))
    longest_round_number = len(str(len(players)))
    ans = ['', '']
    new_results = []
    ids = []
    for y in places:
        for a in y:
            ids.append(a['score'][2])
    results_in_order = [results[x] for x in ids]
    for x in results_in_order:
        new_results.append([])
        for y in ids:
            new_results[-1].append(x[y])
    for x in places:
        display_place = True
        for y in x:
            line = ''
            if display_place:
                line += ' ' * (longest_rank - len(str(cur_line + 1))) + str(cur_line + 1) + '  '
                display_place = False
            else:
                line += ' ' * longest_rank + '  '
            line += y['Player']
            spaces = longest_name - len(y['Player']) + (longest_round_number - 1)
            line += ' ' * spaces
            for x in new_results[cur_line]:
                if x == None:
                    line += ' '
                elif x == 0.5:
                    line += '='
                elif x == 1:
                    line += '1'
                elif x == 0:
                    line += '0'
                line += ' ' * longest_round_number
            line = line[:-longest_round_number]
            len_score = len('{:0.1f}'.format(y['score'][0]))
            len_SB = len('{:0.2f}'.format(y['score'][1]))
            line += ('  ' + ' ' * (longest_score - len_score) + '{:0.1f}' + ' ' * (longest_SB - len_SB + 2) + '{:0.2f}').format(y['score'][0], y['score'][1])
            cur_line += 1
            ans.append(line)
    ans[1] = '=' * len(ans[2])
    ans[0] = ' ' * (longest_rank - 1) + '#  Player' + ' ' * (longest_name - 6 + longest_round_number - 1)
    for x in range(1, len(players) + 1):
        ans[0] += str(x)
        ans[0] += ' ' * (longest_round_number - len(str(x + 1)) + 1)
    ans[0] = ans[0].rstrip()
    ans[0] += '  ' + ' ' * math.floor(longest_score / 3 - 1) + 'Pts' + ' ' * math.ceil(longest_score / 3 - 1)
    ans[0] += '  ' + ' ' * math.floor(longest_SB / 2 - 1) + 'SB'
    return '\n'.join(ans)
