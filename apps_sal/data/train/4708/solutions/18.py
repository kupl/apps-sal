def human_years_cat_years_dog_years(human_years):
    cat_years = 15 if human_years==1 else (15+9 if human_years==2 else 15+9+(human_years-2)*4)
    dog_years = 15 if human_years==1 else (15+9 if human_years==2 else 15+9+(human_years-2)*5)
    return [human_years,cat_years,dog_years]
