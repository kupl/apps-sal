def calculate_age(year_of_birth, current_year):
    if current_year == year_of_birth:
        return "You were born this very year!"
    elif current_year - year_of_birth == 1:
        return "You are 1 year old."
    elif current_year > year_of_birth:
        return "You are {} years old.".format(current_year - year_of_birth)
    elif current_year - year_of_birth == -1:
        return "You will be born in 1 year."
    else:
        return "You will be born in {} years.".format(year_of_birth - current_year)
