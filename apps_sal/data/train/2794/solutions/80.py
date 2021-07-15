def calculate_age(year_of_birth, current_year):
    if year_of_birth == current_year:
        return "You were born this very year!"
    elif (year_of_birth - current_year) == -1:
        return "You are 1 year old."
    elif (year_of_birth - current_year) == 1:
        return "You will be born in 1 year."
    elif year_of_birth < current_year:
        return "You are {} years old.".format(abs(year_of_birth-current_year))
    else:
         return "You will be born in {} years.".format(year_of_birth-current_year)
