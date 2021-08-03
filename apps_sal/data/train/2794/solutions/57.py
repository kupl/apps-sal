def calculate_age(year_of_birth, current_year):
    if year_of_birth - current_year == 1:
        return "You will be born in 1 year."
    elif current_year - year_of_birth == 1:
        return "You are 1 year old."
    elif year_of_birth < current_year:
        return "You are {} years old.".format(current_year - year_of_birth)
    elif year_of_birth > current_year:
        return "You will be born in {} years.".format(year_of_birth - current_year)
    else:
        return "You were born this very year!"
