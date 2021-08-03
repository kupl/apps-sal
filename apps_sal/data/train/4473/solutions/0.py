def xp_to_target_lvl(*args):
    if len(args) < 2:
        return 'Input is invalid.'

    current_xp, target_lvl = args

    if not isinstance(target_lvl, int):
        return 'Input is invalid.'

    if not (0 < target_lvl < 171):
        return 'Input is invalid.'

    if current_xp < 0:
        return 'Input is invalid.'

    level = 1
    xp = 314
    xp_bump = 25

    sum_ = 0
    while level < target_lvl:
        sum_ += xp
        level += 1
        xp_bump_reduction = level // 10
        xp += int(xp * (xp_bump - xp_bump_reduction) / 100)

    diff = sum_ - current_xp
    if diff <= 0:
        return 'You have already reached level {}.'.format(target_lvl)
    else:
        return diff
