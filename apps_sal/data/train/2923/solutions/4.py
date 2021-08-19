def dad_filter(string):
    return ','.join([w for w in string.rstrip(', ').split(',') if w != ''])
