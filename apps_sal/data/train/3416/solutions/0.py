def total_kilometers(cons, petrol):
    return round(100 * petrol / cons, 2)


def check_distance(dist, cons, petrol):
    return 'You will need to refuel' if dist > total_kilometers(cons, petrol) else [[n * 100, dist - 100 * n, round(petrol - cons * n, 2)] for n in range(dist // 100 + 1)]
