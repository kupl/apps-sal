def shorten_to_date(long_date):
    char = long_date.split()[:-1]
    tuple_char = (char[0], char[1], char[2][:-1])
    result = ' '.join(tuple_char)
    return result
