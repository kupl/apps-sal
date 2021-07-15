def human_years_cat_years_dog_years(human_years):
    b = 0
    c = 0
    if human_years == 1:
        b = 15
        c = 15
    elif human_years == 2:
        b = 24
        c = 24
    else:
        b = 24 + (human_years-2)*4
        c = 24 + (human_years-2)*5
    return [human_years,b,c]
