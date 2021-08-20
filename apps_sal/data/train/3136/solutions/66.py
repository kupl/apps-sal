def people_with_age_drink(age):
    kids_age = range(0, 14)
    teens_age = range(14, 18)
    youngadults_age = range(18, 21)
    if age in kids_age:
        return 'drink toddy'
    elif age in teens_age:
        return 'drink coke'
    elif age in youngadults_age:
        return 'drink beer'
    else:
        return 'drink whisky'
