def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age > 1:
        return f"You are {age} years old."
    elif age == 1:
        return f"You are {age} year old."
    elif age == 0:
        return f"You were born this very year!"
    if age == -1:
        return f"You will be born in {-age} year."
    if age < -1:
        return f"You will be born in {-age} years."
