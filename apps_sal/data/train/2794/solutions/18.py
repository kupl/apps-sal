def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    return f"You are {diff} year{'s' * (diff > 1)} old." if diff > 0 else f"You will be born in {-diff} year{'s' * (-diff > 1)}." if diff < 0 else 'You were born this very year!'
