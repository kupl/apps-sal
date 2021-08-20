def diamonds_and_toads(s, f):
    return {k: s.count(k[0]) + 2 * s.count(k[0].upper()) for k in ['crystal', 'python', 'ruby', 'squirrel'][f < 'f'::2]}
