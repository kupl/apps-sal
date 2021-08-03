def conference_picker(cities_visited, cities_offered):
    for i in cities_offered:
        if i not in cities_visited:
            return i
    return "No worthwhile conferences this year!"
