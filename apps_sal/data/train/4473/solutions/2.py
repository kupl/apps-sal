from fractions import Fraction


def xp_to_target_lvl(current_xp=None, target_lvl=None):
    if not isinstance(current_xp, int) or not isinstance(target_lvl, int) or current_xp < 0 or (not 1 <= target_lvl <= 170):
        return 'Input is invalid.'
    (increase, xp, total) = (Fraction(5, 4), 314, 0)
    for i in range(2, target_lvl + 1):
        if not i % 10:
            increase -= Fraction(1, 100)
        (total, xp) = (total + xp, int(xp * increase))
    return total - current_xp if total > current_xp else f'You have already reached level {target_lvl}.'
