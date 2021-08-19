def human_years_cat_years_dog_years(human_years):
    CAT_YEARS_FIRST = 14
    DOG_YEARS_FIRST = 14
    CAT_YEARS_SECOND = 8
    DOG_YEARS_SECOND = 8
    CAT_YEARS_THIRD = 4
    DOG_YEARS_THIRD = 5
    if human_years == 1:
        return [human_years, human_years + CAT_YEARS_FIRST, human_years + DOG_YEARS_FIRST]
    elif human_years == 2:
        return [human_years, human_years + CAT_YEARS_FIRST + CAT_YEARS_SECOND, human_years + DOG_YEARS_FIRST + DOG_YEARS_SECOND]
    else:
        return [human_years, CAT_YEARS_FIRST + CAT_YEARS_SECOND + CAT_YEARS_THIRD * (human_years - 2) + 2, DOG_YEARS_FIRST + DOG_YEARS_SECOND + DOG_YEARS_THIRD * (human_years - 2) + 2]
