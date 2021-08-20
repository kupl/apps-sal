def directions(goal):
    while 'S' in goal and 'N' in goal:
        goal.remove('N')
        goal.remove('S')
    while 'W' in goal and 'E' in goal:
        goal.remove('W')
        goal.remove('E')
    lookup = ['N', 'S', 'E', 'W']

    def key_func(s):
        return (lookup.index(s[0]), s) if s[0] in lookup else (len(lookup), s)
    return sorted(goal, key=key_func)
