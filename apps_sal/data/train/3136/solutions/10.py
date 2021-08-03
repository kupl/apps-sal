def people_with_age_drink(age):
    return 'drink %s' % ('toddy' if age < 14 else 'coke' if 13 < age < 18
                         else 'beer' if 17 < age < 21 else 'whisky')
