def total_licks(env):
    n = 252
    s = ''
    for (k, v) in list(env.items()):
        n += v
        if v > 0:
            if max(env, key=env.get) not in s:
                s += max(env, key=env.get)
    if env == {} or s == '':
        return f'It took {n} licks to get to the tootsie roll center of a tootsie pop.'
    else:
        return f'It took {n} licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was {s}.'
