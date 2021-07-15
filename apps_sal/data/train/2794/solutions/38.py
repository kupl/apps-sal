def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    text = "You were born this very year!"
    if age > 0:
        text = f"You are {age} year{'s'*(age>1)} old."
    elif age<0:
        text = f"You will be born in {abs(age)} year{'s'*(abs(age)>1)}."
    return  text
