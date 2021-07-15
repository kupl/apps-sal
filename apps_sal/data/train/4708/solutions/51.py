def human_years_cat_years_dog_years(human_years):
    cat = 0 
    dog = 0
    if human_years == 1:
        cat, dog = 15, 15
        return [human_years, cat, dog] 
    elif human_years == 2:
        cat, dog = 24, 24
        return [human_years, cat, dog]
    else:
        cat = 24 + ((human_years-2)*4)
        dog = 24 + ((human_years-2)*5)
        return [human_years, cat, dog]
