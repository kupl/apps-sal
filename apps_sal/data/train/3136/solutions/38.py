def people_with_age_drink(age):
    if 0 <= age <= 13:
        return "drink toddy"
    elif 14 <= age <= 17:
        return "drink coke"
    elif 18 <= age <= 20:
        return "drink beer"
    else:
        return "drink whisky"
