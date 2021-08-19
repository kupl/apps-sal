def conference_picker(cities_visited, cities_offered):
    return [city for city in cities_offered + ['No worthwhile conferences this year!'] if city not in cities_visited][0]
