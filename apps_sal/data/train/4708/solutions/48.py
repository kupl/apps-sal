def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    humanYears = human_years
    for i in range(human_years):
        if i == 0:
            catYears = catYears + 15
            dogYears = dogYears + 15
        
        if i == 1:
            catYears = catYears + 9
            dogYears = dogYears + 9
            
        if i > 1:
            catYears = catYears + 4
            dogYears = dogYears + 5
            
    return [humanYears,catYears,dogYears]

