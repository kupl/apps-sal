def optimum_location(students, locations):
    o = min(locations, key=lambda loc: sum(abs(x - loc['x']) + abs(y - loc['y']) for x, y in students))
    return 'The best location is number %s with the coordinates x = %s and y = %s' % (o['id'], o['x'], o['y'])
