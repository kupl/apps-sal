YRS = (15, 15 + 9, (4, 5))


def human_years_cat_years_dog_years(human_years):
    return [human_years, *({0: YRS[0]}.get(human_years - 1, k * (human_years - 2) + YRS[1]) for k in YRS[-1])]
