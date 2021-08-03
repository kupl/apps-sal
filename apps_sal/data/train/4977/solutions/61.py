from functools import reduce


def goals(laLiga, copaDelRey, championsLeague):
    return reduce(lambda x, y: x + y, [laLiga, copaDelRey, championsLeague])
