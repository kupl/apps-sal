def fight(robot_1, robot_2, tactics):
    (attack, defend) = (robot_1, robot_2) if robot_1['speed'] >= robot_2['speed'] else (robot_2, robot_1)
    while attack['health'] > 0:
        if attack['tactics']:
            defend['health'] -= tactics[attack['tactics'].pop()]
        elif not defend['tactics']:
            break
        (attack, defend) = (defend, attack)
    if attack['health'] == defend['health']:
        return 'The fight was a draw.'
    return '{} has won the fight.'.format((defend if attack['health'] < defend['health'] else attack)['name'])
