def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    return "You are {} {} old.".format(diff, "year" if diff == 1 else "years") if diff > 0 else "You will be born in {} {}.".format(-diff, "year" if diff == -1 else "years") if diff < 0 else "You were born this very year!"
