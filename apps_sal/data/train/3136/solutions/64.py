def people_with_age_drink(age):
    drinks = {'toddy': range(14), 'coke': range(14, 18), 'beer': range(18, 21), 'whisky': range(21, 999)}
    for (key, age_range) in drinks.items():
        if age in age_range:
            return f'drink {key}'
