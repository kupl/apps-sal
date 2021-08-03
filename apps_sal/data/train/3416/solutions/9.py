def total_kilometers(cons, petrol):
    return round((petrol * 100) / cons, 2)


def check_distance(distance, cons, petrol):
    if distance > (petrol * 100) / cons:
        return "You will need to refuel"
    else:
        l = []
        length = 0
        for i in range(1 + distance // 100):
            l.append([length, distance, round(petrol, 2)])
            length += 100
            distance -= 100
            petrol -= cons
        return l
