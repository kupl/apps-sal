def people_with_age_drink(age):
    return "drink whisky" if age >= 21 else "drink beer" if 18 <= age <= 20 else "drink coke" if 14 <= age <= 17 else "drink toddy"
