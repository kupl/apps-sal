def conference_picker(cities_visited, cities_offered):
    city = []
    for i in cities_offered:
        if i not in cities_visited:
            city.append(i)
    if len(city) == 0:
        return 'No worthwhile conferences this year!'
    else:
        return city[0]
