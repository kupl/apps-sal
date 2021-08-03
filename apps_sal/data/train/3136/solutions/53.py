def people_with_age_drink(age):
    if age <= 13:
        return "drink toddy"
    elif 14 <= age <= 17:
        return "drink coke"
    elif 18 <= age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"
