def last_chair(n):
    return n - 1
    spots = [[i, False, None, None, None, None] for i in range(n)]

    def clean(n, d=0):
        return n if n is not None else d

    def live(s):
        return not s[1]

    def position(s):
        return s[0]

    def near(s):
        return s[4]

    def spaces(s):
        return s[5]
    while any(filter(live, spots)):
        nearest = None
        for i in range(n):
            if spots[i][1]:
                nearest = 0
            elif nearest is not None:
                nearest += 1
            spots[i][2] = nearest
        nearest = None
        for i in range(n - 1, -1, -1):
            if spots[i][1]:
                nearest = 0
            elif nearest is not None:
                nearest += 1
            spots[i][3] = nearest
        for i in range(n):
            spots[i][4] = min(clean(spots[i][2], n), clean(spots[i][3], n))
            spots[i][5] = clean(spots[i][2]) + clean(spots[i][3])
        options = list(filter(live, spots))
        options.sort(key=near, reverse=True)
        best = near(options[0])
        options = [s for s in options if near(s) == best]
        options.sort(key=spaces, reverse=True)
        best = spaces(options[0])
        options = [s for s in options if spaces(s) == best]
        options.sort(key=position)
        options[0][1] = True
        result = position(options[0])
    return result + 1
