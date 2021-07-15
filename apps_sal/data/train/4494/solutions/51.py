def points(games):
    if not games:
        return 0
    x=games[0]
    if(int(x[0])>int(x[2])):
        return 3+points(games[1:])
    if(x[0]==x[2]):
        return 1+points(games[1:])
    return 0+points(games[1:])

