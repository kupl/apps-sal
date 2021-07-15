def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age < 0:
        return f"You will be born in {abs(age)} {'year' if age == -1 else 'years'}."
    if age == 0:
        return 'You were born this very year!'
    return f"You are {age} {'year' if age == 1 else 'years'} old."
