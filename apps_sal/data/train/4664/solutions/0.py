def conference_picker(cities_visited, cities_offered):
    for city in cities_offered:
        if city not in cities_visited:
            return city
    return 'No worthwhile conferences this year!'
