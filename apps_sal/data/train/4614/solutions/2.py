def scoreboard(who_ate_what):
    for d in who_ate_what:
        d['score'] = 5 * d.get('chickenwings', 0) + 3 * d.get('hamburgers', 0) + 2 * d.get('hotdogs', 0)
    return sorted([{k: d[k] for k in ('name', 'score')} for d in who_ate_what], key=lambda d: (-1 * d['score'], d['name']))
