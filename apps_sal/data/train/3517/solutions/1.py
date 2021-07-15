def parade_time(groups, location, speed, pref):
    result = []
    for i in range(1,len(groups)+1):
        if groups[i-1] == pref:
            result.append((location+i) // speed)
    return result
