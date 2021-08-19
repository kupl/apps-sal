def people_with_age_drink(n):
    return 'drink %s' % ('toddy' if n < 14 else 'coke' if n < 18 else 'beer' if n < 21 else 'whisky')
