def select(memory):
    s = memory.split(',')
    s = [x.strip() for x in s]
    marked = []
    for i, name in enumerate(s):
        if name.startswith('!'):
            marked.append(name)
            if i != len(s) - 1:
                marked.append(s[i + 1])
    for mark in marked:
        if mark.startswith('!'):
            if mark in s:
                s.remove(mark)
            n = mark[1:]
        else:
            n = mark[:]
        if n in s:
            s = [x for x in s if x != n]

    return ', '.join(s)
