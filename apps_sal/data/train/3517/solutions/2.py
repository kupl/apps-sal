def parade_time(groups, location, speed, pref):
    return [(location + pos + 1) // speed for pos in [i for (i, g) in enumerate(groups) if g == pref]]
