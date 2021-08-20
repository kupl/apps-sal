def parade_time(groups, location, speed, pref):
    return [(location + i + 1) // speed for (i, group) in enumerate(groups) if group == pref]
