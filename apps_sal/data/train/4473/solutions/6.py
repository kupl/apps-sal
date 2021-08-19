from math import floor


def xp_to_target_lvl(current_xp=-100, target_lvl=-100):
    if type(current_xp) != int or type(target_lvl) != int or current_xp + target_lvl <= 0 or (target_lvl > 170) or (target_lvl < 1):
        return 'Input is invalid.'
    exp_req = 314
    inc = 25
    level = 1
    exp = 0
    while level < target_lvl:
        level += 1
        if level % 10 == 0:
            inc -= 1
        exp += exp_req
        exp_req = floor(exp_req + exp_req * inc / 100)
    if exp - current_xp <= 0:
        return f'You have already reached level {target_lvl}.'
    return exp - current_xp
