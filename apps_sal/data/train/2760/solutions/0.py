def total_licks(env):
    d = 252
    vm = 0
    for k, v in env.items():
        d += v
        if v > vm:
            vm, km = v, k
    return 'It took ' + str(d) + ' licks to get to the tootsie roll center of a tootsie pop.' + (' The toughest challenge was ' + km + '.' if vm > 0 else '')
