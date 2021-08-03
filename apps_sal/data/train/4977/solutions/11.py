import itertools


def goals(laLiga, copaDelRey, championsLeague):
    return list(itertools.accumulate([laLiga, copaDelRey, championsLeague]))[-1]
