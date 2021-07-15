def total_kilometers(cons, petrol):
    return round(petrol * 100.0 / cons,2)

def check_distance(distance, cons, petrol):
    return [[(100 * n), distance - (100 * n), round(petrol - (cons * n),2)] for n in range(distance/100 + 1)] if total_kilometers(cons, petrol) >= distance else "You will need to refuel"
