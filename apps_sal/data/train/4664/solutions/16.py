def conference_picker(cities_visited, cities_offered):
    t = [i for i in cities_offered if i not in cities_visited]
    return t[0] if len(t) > 0 else 'No worthwhile conferences this year!'
