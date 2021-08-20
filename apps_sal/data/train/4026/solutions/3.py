def optimum_location(students, locations):
    best = min(locations, key=lambda location: distance(students, location))
    return 'The best location is number {id} with the coordinates x = {x} and y = {y}'.format(**best)


def distance(students, location):
    return sum((sum((abs(s[i] - location[j]) for (i, j) in ((0, 'x'), (1, 'y')))) for s in students))
