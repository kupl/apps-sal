def conference_picker(cities_visited, cities_offered):
    return next((city for city in cities_offered if not city in cities_visited), 'No worthwhile conferences this year!')
