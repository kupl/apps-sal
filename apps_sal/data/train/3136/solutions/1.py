def people_with_age_drink(age):
    if age <= 13:
        beverage = 'toddy'
    elif age > 13 and age <= 17:
        beverage = 'coke'
    elif age > 17 and age <= 20:
        beverage = 'beer'
    elif age > 20:
        beverage = 'whisky'
    return 'drink ' + beverage
