def crosstable(players, scores):
    points, le = {j: sum(k or 0 for k in scores[i]) for i, j in enumerate(players)}, len(players)
    SB = {j: sum(points[players[k]] / ([1, 2][l == 0.5]) for k, l in enumerate(scores[i]) if l) for i, j in enumerate(players)}

    SORTED, li = [[i, players.index(i)] for i in sorted(players, key=lambda x: (-points[x], -SB[x], x.split()[1]))], []

    ps = [format(i, '.1f') for i in points.values()]
    Ss = [format(i, '.2f') for i in SB.values()]

    digit = len(str(le))
    name = len(max(players, key=len))
    pts = len(str(max(ps, key=lambda x: len(str(x)))))
    sb = len(str(max(Ss, key=lambda x: len(str(x)))))

    for i, j in enumerate(SORTED):
        ten_ = [" ", "  "][le >= 10]
        index = [str(i + 1), " "][points[j[0]] == points[SORTED[i - 1][0]] and SB[j[0]] == SB[SORTED[i - 1][0]]].rjust(digit)
        name_ = j[0].ljust(name)
        team = ten_.join(['1=0 '[[1, 0.5, 0, None].index(scores[j[1]][l])] or '_' for k, l in SORTED])
        pt = str(format(points[j[0]], ".1f")).rjust(pts)
        Sb = str(format(SB[j[0]], ".2f")).rjust(sb)
        li.append(f'{index}  {name_}{["  ", "   "][le >= 10]}{team}  {pt}  {Sb}')

    fline = ' '.join(['#'.rjust(digit) + '  ' +
                      'Player'.ljust(name) +
                    ['  ', '   '][len(players) >= 10] +
                    ''.join([[' ', '  '][i < 10 and le >= 10] + str(i) for i in range(1, le + 1)]).strip() + '  ' +
                    'Pts'.center(pts) + '  ' +
                    'SB'.center(sb - [0, 2][sb & 1])]).rstrip()
    return '\n'.join([fline, '=' * len(max(li, key=len))] + li)
