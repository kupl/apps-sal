def stringify(n):
    return 'None' if n == None else (lambda s: ([i for i in iter(lambda: ((s['r'].append(str(s['n'].data)), [None for s['n'] in [s['n'].next]]), s['n'] != None)[1], False)], s['r'].append('None'), ' -> '.join(s['r']))[-1])({'r': [], 'n': n})
