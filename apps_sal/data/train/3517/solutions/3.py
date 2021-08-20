def parade_time(groups, location, speed, pref):
    return [(location + i) // speed for (i, g) in enumerate(groups, 1) if g == pref]
