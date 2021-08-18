def light_changes_iter(n, *args):
    '''
    n - no. iterations
    args is a pattern in a form of tuple
    stores the iterations where lights must be changed
    '''
    iteration = 0
    tup = ()
    while True:
        for x in args:
            iteration += x
            tup += (iteration,)
            if max(tup) > n:
                return tup[:-1]


def shift_lights(road_state, init_state):
    '''
    current road_state
    initial_state - list with the indexes of the initial light state
    current_pos - current position of the car to be updated
    pos_index - position of the car
    '''
    temp = road_state.split(" ")

    for index in init_state:
        if temp[0][index] == "O":
            temp[0] = temp[0][:index] + "R" + temp[0][index + 1:]

        elif temp[0][index] == "G":
            temp[0] = temp[0][:index] + "O" + temp[0][index + 1:]

        elif temp[0][index] == "R":
            temp[0] = temp[0][:index] + "G" + temp[0][index + 1:]

    return "".join(temp)


def traffic_lights(road_state, n):
    '''
    road_state is a list with the initial road state
    '''
    road = [] + [road_state]
    road_simulated = "." + road_state[1:]

    green = light_changes_iter(n, 5, 1, 5)
    orange = light_changes_iter(n, 1, 5, 5)
    red = light_changes_iter(n, 5, 5, 1)

    init_green = [i for i, char in enumerate(road_simulated) if char == "G"]
    init_orange = [i for i, char in enumerate(road_simulated) if char == "O"]
    init_red = [i for i, char in enumerate(road_simulated) if char == "R"]

    pos_index = 0

    for ite in range(1, n + 1):
        if ite in green:
            road_simulated = shift_lights(road_simulated, init_green)
        if ite in orange:
            road_simulated = shift_lights(road_simulated, init_orange)
        if ite in red:
            road_simulated = shift_lights(road_simulated, init_red)

        try:
            if road_simulated[pos_index + 1] in ("O", "R"):
                road_state = road_simulated[:pos_index] + "C" + road_simulated[pos_index + 1:]
                road.append(road_state)
                continue

            pos_index += 1
            road_state = road_simulated[:pos_index] + "C" + road_simulated[pos_index + 1:]
            road.append(road_state)

        except IndexError:
            road.append(road_simulated)

    return road
