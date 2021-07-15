def human_years_cat_years_dog_years(hy):
    return [hy, (15 if hy==1 else 24 if hy==2 else 24+(hy-2)*4), (15 if hy==1 else 24 if hy==2 else 24+(hy-2)*5)]
