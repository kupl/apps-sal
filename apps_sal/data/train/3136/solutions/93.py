def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age < 18 and age > 0:
        return 'drink coke'
    elif age < 21 and age > 0:
        return 'drink beer'
    elif age >= 21 and age > 0:
        return 'drink whisky'
