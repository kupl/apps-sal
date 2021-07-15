def human_years_cat_years_dog_years(human_years):
    a=human_years
    if human_years==1:
        d=15
        c=15
    elif human_years==2:
        d=24
        c=24
    else:
        d=24+abs(human_years-2)*5
        c=24+abs(human_years-2)*4
    
    return [a,c,d]
