def human_years_cat_years_dog_years(human_years):
    # Your code here
    catYears = 0
    dogYears = 0
    
    if human_years < 2:
        catYears = human_years * 15
        dogYears = catYears
    elif human_years < 3:
        catYears = 15 + 9
        dogYears = catYears
    else:
        catYears = ((human_years -2) * 4) + 24
        dogYears = ((human_years -2) * 5) + 24
    return [human_years, catYears, dogYears]
