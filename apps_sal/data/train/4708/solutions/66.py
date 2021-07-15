def human_years_cat_years_dog_years(human_years):
    catYears = 15
    dogYears = 15
    if human_years == 1:
        return [human_years,catYears,dogYears]
    elif human_years == 2:
        return [human_years,catYears+9,dogYears+9]
    else:
        return [human_years,catYears+9+(human_years-2)*4,dogYears+9+(human_years-2)*5]
