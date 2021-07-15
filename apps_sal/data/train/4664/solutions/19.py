def conference_picker(cities_visited, cities_offered):
    if len(cities_visited) == 0:
        return cities_offered[0]
    for city in cities_offered:
        if city in cities_visited:
            pass
        else:
            return city
    return 'No worthwhile conferences this year!'
