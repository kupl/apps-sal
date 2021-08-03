def separate_liquids(glass):
    chain = sorted(sum(glass, []), key='OAWH'.index)
    return [chain[len(level) * i:][:len(level)] for i, level in enumerate(glass)]
