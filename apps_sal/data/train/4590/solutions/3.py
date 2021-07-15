def alt_or(lst):
    return eval(str(lst).replace(',', '|'))[0] if lst else None
