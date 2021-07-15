def people_with_age_drink(age):
    if age < 14:
        drink = "toddy"
    elif 14 <= age < 18:
        drink = "coke"
    elif 18 <= age < 21:
        drink = "beer"
    else:
        drink = "whisky"
    return "drink"+ " " + drink
