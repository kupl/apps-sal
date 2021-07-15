def parade_time(groups, location, speed, pref):
    result = []
    for i, x in enumerate(groups):
        if x == pref:
            result.append((location + i + 1) // speed)
    return result
