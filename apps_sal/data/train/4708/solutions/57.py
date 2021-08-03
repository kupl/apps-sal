def human_years_cat_years_dog_years(human):
    if human == 1:
        return [human, 15, 15]
    if human == 2:
        return [human, 24, 24]
    if human >= 3:
        return [human, ((human - 2) * 4) + 24, ((human - 2) * 5) + 24]
