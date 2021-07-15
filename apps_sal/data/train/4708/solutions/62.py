from itertools import accumulate, repeat

def human_years_cat_years_dog_years(years):
    if years >= 2:
        return [years, 4 * (years - 2) + 24, 5 * (years - 2) + 24]
    elif years == 1:
        return [1, 15, 15]
