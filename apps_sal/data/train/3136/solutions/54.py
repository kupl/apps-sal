def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    if age >= 14 and age <= 17:
        return "drink coke"
    if age >= 18 and age <= 20:
        return "drink beer"
    else:
        return "drink whisky"
