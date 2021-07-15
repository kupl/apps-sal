def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    return f"You are {age} year{'s' if age > 1 else ''} old." if age >= 1 \
        else f"You will be born in {abs(age)} year{'s' if age < -1 else ''}." if age < 0 \
        else "You were born this very year!"
