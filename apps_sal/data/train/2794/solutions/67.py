def calculate_age(y, c):
    year = 'years'
    if c + 1 == y or c - 1 == y or c == y:
        year = 'year'
    return 'You are ' + str(c - y) + ' ' + year + ' old.' if c > y else 'You will be born in ' + str(y - c) + ' ' + year + '.' if y > c else 'You were born this very ' + year + '!'
