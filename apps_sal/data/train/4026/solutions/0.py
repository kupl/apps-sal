def optimum_location(students, locations):
    m = min(locations, key=lambda loc: sum((abs(loc['x'] - s[0]) + abs(loc['y'] - s[1]) for s in students)))
    return 'The best location is number %d with the coordinates x = %d and y = %d' % (m['id'], m['x'], m['y'])
