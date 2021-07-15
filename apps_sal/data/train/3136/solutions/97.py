def people_with_age_drink(age):
    if age < 14:
        a = 'drink toddy'
    elif age < 18:
        a = 'drink coke'
    elif age < 21:
        a = 'drink beer'
    else:
        a = 'drink whisky'
    return a

