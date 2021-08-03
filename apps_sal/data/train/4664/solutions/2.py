def conference_picker(cities_visited, cities_offered):

    visited = frozenset(cities_visited)

    for city in cities_offered:
        if city not in visited:
            return city

    return 'No worthwhile conferences this year!'
