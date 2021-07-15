def total_licks(env):
    licks = "It took {} licks to get to the tootsie roll center of a tootsie pop.".format(252 + sum(env.values()))
    toughest_key, toughest_value = max(env.items(), key=lambda item: item[1]) if env else ("", 0)
    toughest_msg = " The toughest challenge was {}.".format(toughest_key) if toughest_value > 0 else ""
    return licks + toughest_msg
