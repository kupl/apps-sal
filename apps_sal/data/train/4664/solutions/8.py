def conference_picker(cities_visited, cities_offered):
    return next((c for c in cities_offered if c not in cities_visited), 'No worthwhile conferences this year!')
