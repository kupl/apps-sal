def optimum_location(students, locations, optimal=(float('inf'),)):
    for loc in locations:
        distance = sum(abs(x - loc['x']) + abs(y - loc['y']) for x, y in students)
        if distance < optimal[0]:
            optimal = distance, loc['id'], loc['x'], loc['y']
    return 'The best location is number %s with the coordinates x = %s and y = %s' % optimal[1:]
