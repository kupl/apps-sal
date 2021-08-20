def xp_to_target_lvl(cur_xp=-1, lvl=-1):
    if not isinstance(cur_xp, int) or cur_xp < 0 or (not isinstance(lvl, int)) or (lvl <= 0) or (lvl > 170):
        return 'Input is invalid.'
    count = 1
    xp = 0
    multipler = 25
    next_lvl = 314
    while count < lvl:
        count += 1
        if count == lvl:
            xp += next_lvl
            print(xp, count)
            break
        if count % 10 == 0:
            multipler = float(multipler - 1)
        xp += next_lvl
        next_lvl = next_lvl + int(next_lvl * (multipler / 100))
        print(xp, count, multipler)
    result = xp - cur_xp
    if result > 0:
        return result
    else:
        return f'You have already reached level {lvl}.'
