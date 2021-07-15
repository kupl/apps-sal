def calculate_age(year_of_birth, current_year):
    if year_of_birth > current_year:
            diff = year_of_birth - current_year
            if diff == 1:
                return f"You will be born in {diff} year."
            else:
                return f"You will be born in {diff} years."
    elif year_of_birth == current_year:
        return "You were born this very year!"
    else:
        diff = current_year - year_of_birth
        if diff == 1:
            return f"You are {diff} year old."
        else:
            return f"You are {diff} years old."
