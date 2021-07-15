def total_licks(env):
    tough = max(env.items(), key=lambda x:x[1]) if env else [0, 0]
    total = sum(v for v in env.values())
    
    output = 'It took {} licks to get to the tootsie roll center of a tootsie pop.'.format(252 + total)
    if tough[1] > 0:
        output += ' The toughest challenge was {}.'.format(tough[0])
    return output
