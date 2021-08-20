def select(memory):
    hates = set()
    h = False
    for name in memory.split(', '):
        if name.startswith('!'):
            hates.add(name.lstrip('!'))
            h = True
        elif h:
            hates.add(name.lstrip('!'))
            h = False
    return ', '.join((name for name in memory.split(', ') if name.lstrip('!') not in hates))
