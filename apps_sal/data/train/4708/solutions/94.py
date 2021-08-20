def human_years_cat_years_dog_years(yr):
    return ['one-liner', [1, 15, 15], [2, 24, 24]][yr] if yr in range(1, 3) else [yr, (yr - 2) * 4 + 24, (yr - 2) * 5 + 24]
