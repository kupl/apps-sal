def directions(goal):

    y = goal.count('N') - goal.count('S')
    x = goal.count('E') - goal.count('W')

    ns = 'N' if y > 0 else 'S'
    ew = 'E' if x > 0 else 'W'

    return [_ for _ in abs(y) * ns + abs(x) * ew]
