import numpy as np

def goals(laLiga, copaDelRey, championsLeague):
    a = np.array((laLiga, copaDelRey, championsLeague))
    return sum(a)
