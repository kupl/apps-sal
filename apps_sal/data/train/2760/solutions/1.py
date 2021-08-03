from operator import itemgetter

TOTAL_LICKS = 252


def total_licks(env):
    message = ('It took %d licks to get to the tootsie roll center of a tootsie pop.' %
               (TOTAL_LICKS + sum(env.values())))

    if env:
        toughest_challenge = max(iter(env.items()), key=itemgetter(1))
        if toughest_challenge[1] > 0:
            message += ' The toughest challenge was %s.' % toughest_challenge[0]

    return message
