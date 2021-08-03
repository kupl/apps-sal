def calculate_age(year_of_birth, current_year):
    dif = year_of_birth - current_year
    return "You " + ["are {} year{} old.", "will be born in {} year{}."][dif > 0].format(abs(dif), "s" * (abs(dif) != 1)) if dif else "You were born this very year!"
