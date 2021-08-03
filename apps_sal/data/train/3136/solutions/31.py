def people_with_age_drink(age):
    drink = ""
    if age < 14:
        drink = "drink toddy"
    elif age < 18 and age > 13:
        drink = "drink coke"
    elif age < 21 and age > 17:
        drink = "drink beer"
    else:
        drink = "drink whisky"
    return drink
