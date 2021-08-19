def fight(robot_1, robot_2, tactics):
    if robot_1['speed'] >= robot_2['speed']:
        while robot_2['tactics'] or robot_1['tactics']:
            try:
                robot_2['health'] -= tactics[robot_1['tactics'].pop(0)]
            except:
                pass
            if robot_2['health'] <= 0:
                return 'Rocky has won the fight.'
            try:
                robot_1['health'] -= tactics[robot_2['tactics'].pop(0)]
            except:
                pass
            if robot_1['health'] <= 0:
                return 'Missile Bob has won the fight.'
    else:
        while robot_2['tactics'] or robot_1['tactics']:
            try:
                robot_1['health'] -= tactics[robot_2['tactics'].pop(0)]
            except:
                pass
            if robot_1['health'] <= 0:
                return 'Missile Bob has won the fight.'
            try:
                robot_2['health'] -= tactics[robot_1['tactics'].pop(0)]
            except:
                pass
            if robot_2['health'] <= 0:
                return 'Rocky has won the fight.'
    if robot_1['health'] > robot_2['health']:
        return 'Rocky has won the fight.'
    elif robot_2['health'] > robot_1['health']:
        return 'Missile Bob has won the fight.'
    return 'The fight was a draw.'
