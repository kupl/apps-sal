def people_with_age_drink(age):
    return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')
