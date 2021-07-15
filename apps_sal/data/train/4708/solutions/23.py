def human_years_cat_years_dog_years(hy):
    cy = 15 + (hy > 1) * (4 * hy + 1)
    dy = 15 + (hy > 1) * (5 * hy - 1)
    return [hy, cy, dy]
