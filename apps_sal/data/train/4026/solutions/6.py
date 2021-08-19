def optimum_location(students, locations):
    return 'The best location is number %(id)d with the coordinates x = %(x)d and y = %(y)d' % min(locations, key=lambda l: sum((abs(x - l['x']) + abs(y - l['y']) for (x, y) in students)))
