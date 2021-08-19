def goals(laLiga, copaDelRey, championsLeague):
    if laLiga >= 0 and copaDelRey >= 0 and (championsLeague >= 0):
        return laLiga + copaDelRey + championsLeague
    else:
        print('the input will always be valid')
