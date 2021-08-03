THICKNESS = 0.0001


def fold_to(distance):
    if distance < 0:
        return None
    current_thick = THICKNESS
    time = 0
    while current_thick < distance:
        current_thick += current_thick
        time += 1
    return time
