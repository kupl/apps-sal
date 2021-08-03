def calculate_age(year_of_birth, current_year):
    if current_year - year_of_birth > 1:
        return f"You are {current_year - year_of_birth} years old."
    elif current_year - year_of_birth == 1:
        return f"You are {current_year - year_of_birth} year old."
    elif current_year - year_of_birth == -1:
        return f"You will be born in {-(current_year - year_of_birth)} year."
    elif current_year - year_of_birth < -1:
        return f"You will be born in {-(current_year - year_of_birth)} years."
    else:
        return "You were born this very year!"
