def people_with_age_drink(age):
    return 'drink {}'.format('toddy' if age < 14 else 'coke' if 18 > age >= 14 else 'beer' if 21 > age >= 18 else 'whisky')
