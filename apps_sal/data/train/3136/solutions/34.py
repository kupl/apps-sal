def people_with_age_drink(age):
    drink = 'drink'
    if age < 14:
        drink = '{} toddy'.format(drink)
    elif age < 18:
        drink = '{} coke'.format(drink)
    elif age < 21:
        drink = '{} beer'.format(drink)
    else:
        drink = '{} whisky'.format(drink)
    return drink
