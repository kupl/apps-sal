def fight(robot_1, robot_2, tactics):
    # your code
    robot1_health = robot_1['health']
    robot2_health = robot_2['health']
    if len(robot_1['tactics']) < len(robot_2['tactics']):
        return '{} has won the fight.'.format(robot_2['name'])
    elif len(robot_1['tactics']) > len(robot_2['tactics']):
        return '{} has won the fight.'.format(robot_1['name'])
    else:
        if robot_1['speed'] < robot_2['speed']:
            for tactic in zip(robot_1['tactics'], robot_2['tactics']):
                robot1_health -= tactics[tactic[1]]
                if robot1_health <= 0:
                    return '{} has won the fight.'.format(robot_2['name'])
                robot2_health -= tactics[tactic[0]]
                if robot2_health <= 0:
                    return '{} has won the fight.'.format(robot_1['name'])
        else:
            for tactic in zip(robot_1['tactics'], robot_2['tactics']):
                robot2_health -= tactics[tactic[0]]
                if robot2_health <= 0:
                    return '{} has won the fight.'.format(robot_1['name'])
                robot1_health -= tactics[tactic[1]]
                if robot1_health <= 0:
                    return '{} has won the fight.'.format(robot_2['name'])
    if robot1_health < robot2_health:
        return '{} has won the fight.'.format(robot_2['name'])
    elif robot1_health > robot2_health:
        return '{} has won the fight.'.format(robot_1['name'])
    else:
        return "The fight was a draw."
