def people_with_age_drink(age):
    return f"drink {age < 14 and 'toddy' or (age < 18 and 'coke') or (age < 21 and 'beer') or 'whisky'}"
