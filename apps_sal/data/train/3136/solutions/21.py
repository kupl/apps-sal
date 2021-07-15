def people_with_age_drink(age):
    return ["drink toddy", "drink coke", "drink beer", "drink whisky"][(age >= 21) + (age > 17) + (age > 13)]
    

