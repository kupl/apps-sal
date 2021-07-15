def filter_numbers(string):
    return "".join(x for x in string if not x.isdigit())
