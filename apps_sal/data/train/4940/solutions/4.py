ANIMS = {'H': ['A', 'V'], 'R': ['V'], 'C': ['~']}

def shut_the_gate(farm):
    print(farm)
    f = list(farm)
    rng = list(range(0, len(f)))
    for i in rng:
        if f[i] in ANIMS:
            for food in ANIMS[f[i]]:
                j = 0
                idx = index_of(f, j, food)
                while idx is not None:
                    if idx < i and '|' not in f[idx:i]:
                        f[idx] = '.'
                    elif i < idx and '|' not in f[i:idx]:
                        f[idx] = '.'
                    elif '|' not in f[:i] and '|' not in f[idx:]:
                        f[idx] = '.'
                    elif '|' not in f[i:] and '|' not in f[:idx]:
                        f[idx] = '.'
                    j += 1
                    idx = index_of(f, j, food)

    for i in rng:
        if f[i] in ANIMS:
            if '|' not in f[i:] or '|' not in f[:i]:
                f[i] = '.'
    return ''.join(f)

def index_of(farm, j, food):
    try:
        return farm[j:].index(food) + j
    except:
        return None


