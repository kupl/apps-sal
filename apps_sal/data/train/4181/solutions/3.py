def filter_numbers(stg):
    return ''.join((x for x in stg if not x.isdecimal()))
