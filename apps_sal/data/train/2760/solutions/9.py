def total_licks(env):
    licks = 252 + sum(env.values())
    challenge = max(([v, k] for (k, v) in env.items() if v > 0), default=None)
    result = f'It took {licks} licks to get to the tootsie roll center of a tootsie pop.'
    if challenge:
        result += f' The toughest challenge was {challenge[1]}.'
    return result
