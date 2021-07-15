def calculate_age(year_of_birth, current_year):
    diff = year_of_birth - current_year
    if diff == 0:
        return "You were born this very year!"
    elif  diff > 0:
        return "You will be born in {} {}.".format(diff, "year" if diff == 1 else "years")
    elif diff < 0:
        return "You are {} {} old.".format(abs(diff), "year" if diff == -1 else "years")
