def people_with_age_drink(age):
    drink = ('toddy', 'coke', 'beer', 'whisky')[(age >= 14) + (age >= 18) + (age >= 21)]
    return 'drink {}'.format(drink)
