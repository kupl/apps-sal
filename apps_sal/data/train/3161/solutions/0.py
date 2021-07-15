def select(memory):
    lst = memory.split(', ')
    bad = {who.strip('!') for prev,who in zip(['']+lst,lst+[''])  if who.startswith('!') or prev.startswith('!')}
    return ', '.join(who for who in map(lambda s: s.strip('!'), lst) if who not in bad)
