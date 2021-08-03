def human_years_cat_years_dog_years(h):
    l = list(range(1, h + 1))
    return [h, 15 * len(l[0:1]) + 9 * len(l[1:2]) + 4 * len(l[2:]), 15 * len(l[0:1]) + 9 * len(l[1:2]) + 5 * len(l[2:])]
