def people_with_age_drink(age):
    drinks = ["drink toddy", "drink coke", "drink beer", "drink whisky"]
    if age < 14:
        return drinks[0]
    elif 14 <= age < 18:
        return drinks[1]
    elif 18 <= age < 21:
        return drinks[2]
    else:
        return drinks[3]
