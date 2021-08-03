def total_kilometers(cons, petrol):
    return round(petrol / cons * 100, 2)


def check_distance(distance, cons, petrol):
    if total_kilometers(cons, petrol) < distance:
        return "You will need to refuel"
    return[[i * 100, distance - i * 100, round(petrol - cons * i, 2)]for i in range(0, distance // 100 + 1)]
