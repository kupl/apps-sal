reprs = {60 * 60 * 24 * 7: 'week', 60 * 60 * 24: 'day', 60 * 60: 'hour', 60: 'minute', 1: 'second'}


def to_pretty(seconds):
    for (k, v) in sorted(reprs.items(), key=lambda x: x[0], reverse=True):
        if seconds >= k:
            res = seconds // k
            if res == 1:
                time = 'a'
                if v[int(v[0] == 'h')] in 'aeiou':
                    time += 'n'
            else:
                time = str(int(res))
            if res == 1:
                mult = v
            else:
                mult = v + 's'
            return '{} {} ago'.format(time, mult)
    return 'just now'
