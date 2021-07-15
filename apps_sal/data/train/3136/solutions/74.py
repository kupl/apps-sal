def people_with_age_drink(age):
    rv =  'drink '
    if age < 14:
        return rv + 'toddy'
    elif age < 18:
        return rv + 'coke'
    elif age < 21:
        return rv + 'beer'
    else:
        return rv + 'whisky'

