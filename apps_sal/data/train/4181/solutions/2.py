def filter_numbers(s):
    return ''.join((x for x in s if not x.isdigit()))
