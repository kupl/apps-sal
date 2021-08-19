def people_with_age_drink(age: int) -> str:
    DRINK_TABLE = ((21, 'whisky'), (18, 'beer'), (14, 'coke'), (0, 'toddy'))
    for (limit, drink) in DRINK_TABLE:
        if age >= limit:
            return f'drink {drink}'
    return 'no drink'
