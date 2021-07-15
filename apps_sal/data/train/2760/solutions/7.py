def total_licks(env):
    licks = 252
    if env == {}:
        return f"It took {licks} licks to get to the tootsie roll center of a tootsie pop."
    for challenge in env.items():
        licks += challenge[1]
    max_challenge = max(env.values())
    if max_challenge < 0:
        return f"It took {licks} licks to get to the tootsie roll center of a tootsie pop."
    for cha in env.keys():
        if env[cha] == max_challenge:
            challenge = cha
    return f"It took {licks} licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was {challenge}."
