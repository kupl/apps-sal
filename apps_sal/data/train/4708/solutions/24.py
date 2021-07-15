def human_years_cat_years_dog_years(human_years):
    cat = sum([15,9,(human_years-2)*4][:human_years])
    dog = sum([15,9,(human_years-2)*5][:human_years])
    return [human_years, cat, dog]
