def tv_remote(s):
    d = {y: (i, x) for i, j in enumerate(["abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/", "# *!$%^&"]) for x, y in enumerate(j)}
    def does(a, b): return (abs(d[a][0] - d[b][0]) + (abs(d[a][1] - d[b][1]))) + 1
    status, c = False, 0
    for i, j in zip(s, 'a' + s):
        t, t1 = i.lower(), j.lower()
        if i.isupper():
            if not status:
                t1, status, c = "#", 1, c + does('#', t1)
        elif i.islower():
            if status:
                t1, status, c = '#', 0, c + does('#', t1)
        c += does(t1, t)
    return c
