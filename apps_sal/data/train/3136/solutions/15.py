def people_with_age_drink(age):
    return 'drink ' + next(d for a, d in [
        (21, 'whisky'), (18, 'beer'), (14, 'coke'), (0, 'toddy')
        ] if age >= a)
