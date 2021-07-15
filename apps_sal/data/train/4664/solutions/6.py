def conference_picker(cities_visited, cities_offered):
    picks = (city for city in cities_offered if city not in set(cities_visited))
    try:
        return next(picks)
    except StopIteration:
        return 'No worthwhile conferences this year!'
