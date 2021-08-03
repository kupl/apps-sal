def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    for i in range(1, human_years + 1):
        cat_years += {1: 15, 2: 9}.get(i, 4)
        print(i)
    return [human_years, cat_years, cat_years + (human_years - 2 if human_years > 1 else 0)]
