def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age <= 17 and age >= 14:
        return 'drink coke'
    elif age > 17 and age <= 20:
        return 'drink beer'
    elif age > 20:
        return 'drink whisky'
    else:
        return ''
