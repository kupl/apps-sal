def calculate_age(birth_year, this_year):
    (results, plural) = (this_year - birth_year, '')
    if abs(results) != 1:
        plural = 's'
    if results > 0:
        return 'You are %s year%s old.' % (results, plural)
    elif results < 0:
        return 'You will be born in %s year%s.' % (abs(results), plural)
    elif results == 0:
        return 'You were born this very year!'
