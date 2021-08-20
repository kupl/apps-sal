def fight(robot_1, robot_2, tactics):
    if robot_2['speed'] > robot_1['speed']:
        robot_first = robot_2
        robot_second = robot_1
    else:
        robot_first = robot_1
        robot_second = robot_2
    while len(robot_first['tactics']) > 0 or len(robot_second['tactics']) > 0:
        if len(robot_first['tactics']) > 0:
            robot_second['health'] -= tactics[robot_first['tactics'].pop(0)]
        if robot_second['health'] <= 0:
            return f"{robot_first['name']} has won the fight."
        if len(robot_second['tactics']) > 0:
            robot_first['health'] -= tactics[robot_second['tactics'].pop(0)]
        if robot_first['health'] <= 0:
            return f"{robot_second['name']} has won the fight."
    else:
        if robot_first['health'] == robot_second['health']:
            return 'The fight was a draw.'
        else:
            winner = robot_first['name'] if robot_first['health'] > robot_second['health'] else robot_second['name']
            return f'{winner} has won the fight.'
