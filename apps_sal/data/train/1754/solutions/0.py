def valid(a):
    d = {}
    day_length = len(a[0])
    group_size = len(a[0][0])
    golfers = {g for p in a[0] for g in p}

    for day in a:
        if len(day) != day_length:
            return False
        for group in day:
            if len(group) != group_size:
                return False
            for player in group:
                if player not in golfers:
                    return False
                if player not in d:
                    d[player] = set(group)
                else:
                    if len(d[player] & set(group)) > 1:
                        return False
                    else:
                        d[player].add(group)
    return True
