def dad_filter(string):
    return ','.join([el for el in string.split(',') if el]).rstrip(', ')
