def xp_to_target_lvl(current_xp='', target_lvl=''):
    # good luck ^_^
    if isinstance(current_xp, int) and isinstance(target_lvl, int):
        if current_xp >= 0 and 1 <= target_lvl <= 170:
            a = [314]
            for i in range(2, target_lvl + 2):
                a.append(int(a[-1] * (1.25 - 0.01 * (i // 10))))
            return sum(a[:target_lvl - 1]) - current_xp if sum(a[:target_lvl - 1]) - current_xp > 0 else 'You have already reached level {}.'.format(target_lvl)
    return 'Input is invalid.'
