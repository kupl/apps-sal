def calculate_age(year_of_birth, current_year):
    difference=current_year-year_of_birth
    if difference<0:
        return "You will be born in " +str(abs(difference))+" years." if difference!=-1 else "You will be born in 1 year."
    elif difference>0:
        return "You are " +str(difference)+" years old." if difference!=1 else "You are 1 year old."
    return "You were born this very year!"
