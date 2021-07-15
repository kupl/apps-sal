def human_years_cat_years_dog_years(hy):
    base = 15 * (hy >= 1) + 9 * (hy >= 2)
    rest = max(0, hy - 2)
    
    cy = base + 4 * rest
    dy = base + 5 * rest
    
    return [hy, cy, dy]
