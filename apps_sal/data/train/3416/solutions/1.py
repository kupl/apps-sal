def total_kilometers(cons, petrol): 
    distance = round(((petrol/cons) * 100), 2)
    return distance


def check_distance(distance, cons, petrol):
    outp = []
    track = 0
    driven_dist = 0
    if distance > ((petrol/cons) * 100):
        return 'You will need to refuel'
    while track <= distance:
        outp.append([driven_dist, distance - driven_dist, round(petrol, 2)])
        driven_dist += 100
        petrol -= cons
        track += 100
    return outp


