def total_kilometers(cons, petrol):
    return round(float(petrol) / cons * 100, 2)


def check_distance(distance, cons, petrol):
    if distance * cons > petrol * 100:
        return "You will need to refuel"
    return [[i, distance - i, round(petrol - i * cons / 100, 2)] for i in xrange(0, distance + 1, 100)]
