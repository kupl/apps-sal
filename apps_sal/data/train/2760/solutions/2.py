def total_licks(env):
    s = 'It took {} licks to get to the tootsie roll center of a tootsie pop.'.format(252 + sum(env.values()))
    if any((x > 0 for x in env.values())):
        key = max(env, key=env.get)
        s += ' The toughest challenge was {}.'.format(key)
    return s
