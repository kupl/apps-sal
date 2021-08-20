def select(memory):
    names = memory.split(', ')
    hated = set()
    for (i, name) in enumerate(names):
        if name[0] == '!' or (i > 0 and names[i - 1][0] == '!'):
            hated.update(['!' + name.strip('!'), name.strip('!')])
    return ', '.join(filter(lambda name: name not in hated, names))
