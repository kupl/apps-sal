def calculate_age(year_of_birth, current_year):
    x = current_year - year_of_birth
    if x < 0:
        return f"You will be born in {abs(x)} year{'s' if abs(x)>1 else ''}."
    if x == 0:
        return "You were born this very year!"
    return f"You are {x} year{'s' if x > 1 else ''} old."
