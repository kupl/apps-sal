def total_licks(env):
    sLicks = f"It took {252 + sum(env.values())} licks to get to the tootsie roll center of a tootsie pop."
    if env and max(env.values()) > 0:
        sLicks += f" The toughest challenge was {max(env, key = env.get)}."
    return sLicks
