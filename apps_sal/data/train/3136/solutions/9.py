def people_with_age_drink(age):
    drinks = {age < 14: 'toddy', 14 <= age < 18: 'coke', 18 <= age < 21: 'beer', age >= 21: 'whisky'}
    return 'drink {}'.format(drinks[True])
