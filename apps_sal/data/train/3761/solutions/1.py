def strange_coach(players):
    d = {l: 0 for l in map(chr, range(97, 123))}
    for i in players:
        d[i[0]] += 1
    r = ''.join(sorted((x for x in d if d[x] > 4)))
    return r if r != '' else 'forfeit'
