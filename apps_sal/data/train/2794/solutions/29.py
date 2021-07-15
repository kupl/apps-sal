def calculate_age(year_of_birth, current_year):
    
    age = current_year - year_of_birth
    
    if age == 0:
        return "You were born this very year!"
    
    if age > 0:
        return f"You are {age} year{'s' if age != 1 else ''} old."
    
    if age < 0:
        return f"You will be born in {-age} year{'s' if age != -1 else ''}."

