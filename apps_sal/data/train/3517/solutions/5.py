def parade_time(groups, location, speed, pref):
    return [int((1 + location + i) / speed) for i, g in enumerate(groups) if g == pref]

