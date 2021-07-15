def human_years_cat_years_dog_years(human):
    if human >= 1:
        cat = 15
        dog = 15
    if human  >= 2:
        cat += 9
        dog += 9
    if human >= 3:
        cat += 4*(human-2)
        dog += 5*(human-2)
        
    return [human,cat,dog]
