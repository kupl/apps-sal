def target_game(values):
    max_can_shoot, max_can_not_shoot = 0, 0
    for val in values:
        new = max_can_shoot + val
        max_can_shoot = max(max_can_not_shoot, new)
        max_can_shoot, max_can_not_shoot = max_can_not_shoot, max_can_shoot
    return max(max_can_shoot, max_can_not_shoot)
