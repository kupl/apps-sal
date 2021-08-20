def parade_time(groups, location, speed, pref):
    return [c // speed for (c, p) in enumerate(groups, 1 + location) if p == pref]
