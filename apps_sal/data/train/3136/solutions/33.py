def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    if age > 13 and age < 18:
        return 'drink coke'
    if age > 17 and age < 21:
        return 'drink beer'
    if age > 20:
        return 'drink whisky'
