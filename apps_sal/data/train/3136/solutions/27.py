def people_with_age_drink(age):
    return ["drink toddy", "drink coke", "drink beer", "drink whisky"][(age >= 21) + (age >= 18) + (age >= 14)]
