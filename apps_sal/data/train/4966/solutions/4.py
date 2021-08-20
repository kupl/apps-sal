import pprint


def fight(robot_1, robot_2, tactics):
    if robot_1['speed'] < robot_2['speed']:
        (robot_1, robot_2) = (robot_2, robot_1)
    robot_1_turn = True
    while (robot_1['health'] > 0 and robot_2['health'] > 0) and (len(robot_1['tactics']) > 0 or len(robot_2['tactics']) > 0):
        if robot_1_turn and len(robot_1['tactics']) > 0:
            robot_2['health'] -= tactics[robot_1['tactics'][0]]
            robot_1['tactics'].pop(0)
        elif len(robot_2['tactics']) > 0:
            robot_1['health'] -= tactics[robot_2['tactics'][0]]
            robot_2['tactics'].pop(0)
        robot_1_turn = not robot_1_turn
    if robot_1['health'] <= 0 or robot_1['health'] < robot_2['health']:
        return robot_2['name'] + ' has won the fight.'
    elif robot_2['health'] <= 0 or robot_2['health'] < robot_1['health']:
        return robot_1['name'] + ' has won the fight.'
    else:
        return 'The fight was a draw.'
