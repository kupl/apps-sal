def total_kilometers(cons, petrol):
    return round(petrol * 100.0 / cons, 2)


def check_distance(distance, cons, petrol):
    if total_kilometers(cons, petrol) < distance:
        return 'You will need to refuel'
    return [[round(x, 2) for x in (i * 100, distance - i * 100, petrol - cons * i)] for i in range(int(distance / 100) + 1)]
