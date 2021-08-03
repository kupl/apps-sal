def people_with_age_drink(age):

    if age < 14:
        drink = "toddy"
    elif 14 <= age <= 17:
        drink = "coke"
    elif 18 <= age <= 20:
        drink = "beer"
    else:
        drink = "whisky"

    return "drink {}".format(drink)
