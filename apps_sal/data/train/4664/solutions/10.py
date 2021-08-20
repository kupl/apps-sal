def conference_picker(cities_visited, cities_offered):
    SECSR = list(cities_visited)
    confPicker = list(cities_offered)
    shortList = list()
    for city in confPicker:
        if city not in SECSR:
            shortList.append(city)
        else:
            pass
    if len(shortList) > 0:
        return shortList[0]
    else:
        return 'No worthwhile conferences this year!'
