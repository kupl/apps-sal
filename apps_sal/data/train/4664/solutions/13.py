def conference_picker(cities_visited, cities_offered):
    worthwile = set(cities_offered) - set(cities_visited)
    if worthwile:
        return min(worthwile, key=cities_offered.index)
    return 'No worthwhile conferences this year!'
