def calculate_age(year_of_birth, current_year):
    work = current_year - year_of_birth
    if work == 1:
        return "You are 1 year old."
    elif work > 0:
        return "You are {} years old.".format(work)
    elif work == 0:
        return "You were born this very year!"
    elif work == -1:
        return "You will be born in 1 year."
    elif work < 0:
        return "You will be born in {} years.".format(-work)
