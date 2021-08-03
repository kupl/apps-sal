def total_kilometers(cons, petrol):
    result = round(float(petrol) / float(cons) * 100.0, 2)
    print(f'total_kilometers({cons}, {petrol}) => {result}')
    return result


def check_distance(distance, cons, petrol):
    if petrol / cons * 100 < distance:
        return "You will need to refuel"

    result = [[0, distance, petrol]]

    fuel = petrol
    since_start = 0
    to_end = distance
    for _ in range(to_end // 100):
        fuel -= cons
        since_start += 100
        to_end -= 100
        result.append([since_start, to_end, round(fuel, 2)])
    print(f'check_distance({distance}, {cons}, {petrol}) => {result}')
    return result
