def human_years_cat_years_dog_years(y):
    return [y,24+4*(y-2),24+5*(y-2)] if y>=2 else [y,y*9+6,y*9+6]
