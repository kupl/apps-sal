def conference_picker(cities_visited, cities_offered):
    for city in cities_offered:
        if not city in cities_visited:
            return city
    return 'No worthwhile conferences this year!'
