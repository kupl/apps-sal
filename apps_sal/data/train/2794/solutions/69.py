def calculate_age(year_of_birth, current_year):
    return "You were born this very year!" if year_of_birth == current_year else "You are {} year{} old.".format(current_year - year_of_birth, "s" if current_year - year_of_birth != 1 else "") if current_year > year_of_birth else "You will be born in {} year{}.".format(year_of_birth - current_year, "s" if current_year - year_of_birth != -1 else "")
