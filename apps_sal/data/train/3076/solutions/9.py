def solve(arr):
    t1, t2 = [], []
    for i in arr:
        t1.append(' '.join(i.split(' ')[:2]))
        t2.append(' '.join(i.split(' ')[2:]))
    print(t1, t2)
    t2 = t2[::-1]
    t1 = t1[::-1]
    for i in range(len(t1)):
        if "Right" in t1[i]:
            t1[i] = t1[i].replace('Right', 'Left')
        elif "Left" in t1[i]:
            t1[i] = t1[i].replace('Left', 'Right')
    t1 = [t1[-1]] + t1[:-1]
    return ["%s %s" % (e, f) for e, f in zip(t1, t2)]
