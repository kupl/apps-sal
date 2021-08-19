def fight(robot_1, robot_2, tactics):
    if robot_1['speed'] >= robot_2['speed']:
        active = robot_1
        passive = robot_2
    else:
        (active, passive) = (robot_2, robot_1)
    while robot_1['tactics'] or robot_2['tactics']:
        if active['tactics']:
            move = active['tactics'].pop()
            passive['health'] -= tactics[move]
            if passive['health'] <= 0:
                return active['name'] + ' has won the fight.'
        (active, passive) = (passive, active)
    if robot_1['health'] > robot_2['health']:
        return robot_1['name'] + ' has won the fight.'
    elif robot_2['health'] > robot_1['health']:
        return robot_2['name'] + ' has won the fight.'
    else:
        return 'The fight was a draw.'
