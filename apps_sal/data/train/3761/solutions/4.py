from string import ascii_lowercase as az


def strange_coach(players):
    d = dict.fromkeys(az, 0)
    for i in range(len(players)):
        d[players[i][0]] += 1
    s = (''.join([k for k, v in d.items() if v >= 5]))
    return s if s else 'forfeit'
