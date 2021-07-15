def calculate_age(birth_year, current_year):
    results, plural = current_year-birth_year, ''
    
    if abs(results) != 1:
        plural = 's'
        
    if results > 0: 
        out = 'You are %s year%s old.' % (results, plural)
    elif results == 0: 
        out = 'You were born this very year!'
    else:
        out = 'You will be born in %s year%s.' % (abs(results), plural)
    return out
