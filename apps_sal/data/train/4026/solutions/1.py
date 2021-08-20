def manhattan(p1, p2):
    return sum((abs(b - a) for (a, b) in zip(p1, p2)))


def optimum_location(students, locations):
    return 'The best location is number {id:} with the coordinates x = {x:} and y = {y:}'.format(**min((loc for loc in locations), key=lambda l: sum((manhattan(s, (l['x'], l['y'])) for s in students))))
