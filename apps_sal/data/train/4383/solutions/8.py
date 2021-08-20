def artificial_rain(garden):
    if not garden:
        return 0
    sect_cnt = len(garden)
    if sect_cnt < 3:
        return sect_cnt
    best_coverage = 1
    coverages = [2, 1] if garden[0] > garden[1] else [1, 2]
    bump_at = 0 if garden[0] > garden[1] else 1
    coverages += [1] * (sect_cnt - 2)
    for i in range(2, sect_cnt):
        (left_height, height) = (garden[i - 1], garden[i])
        if height > left_height:
            coverages[i] += coverages[i - 1]
            bump_at = i
        elif height == left_height:
            coverages[i - 1] += 1
            coverages[i] = coverages[i - 1]
            if i - 1 != bump_at:
                coverages[bump_at] += 1
            else:
                bump_at = i
        else:
            coverages[bump_at] += 1
        if coverages[bump_at] > best_coverage:
            best_coverage = coverages[bump_at]
    return best_coverage
