def total_kilometers(cons, petrol):
    return round(100 * petrol / cons, 2)


def check_distance(distance, cons, petrol):
    if total_kilometers(cons, petrol) < distance:
        return 'You will need to refuel'
    r = [[0, distance, petrol]]
    x = 0
    while distance >= 100:
        petrol -= cons
        distance -= 100
        x += 100
        r.append([x, distance, round(petrol, 2)])
    return r
