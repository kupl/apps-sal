def xp_to_target_lvl(current_xp=None, target_lvl=None):
    invalid = 'Input is invalid.'
    if type(target_lvl) is not int or type(current_xp) is not int:
        return invalid
    if current_xp < 0 or target_lvl < 1 or target_lvl > 170:
        return invalid
    if target_lvl == 1:
        return 'You have already reached level 1.'
    needed_xp = 314
    if target_lvl > 2:
        needed_xp = calc_needed(target_lvl)
    if current_xp >= needed_xp:
        return 'You have already reached level %s.' % target_lvl
    return needed_xp - current_xp


def calc_needed(target_lvl):
    increase = 25
    lvl_xp = needed_xp = 314
    for lvl in range(3, target_lvl + 1):
        lvl_xp += int(lvl_xp * increase / 100)
        needed_xp += lvl_xp
        if lvl % 10 == 0:
            increase -= 1
    return needed_xp
