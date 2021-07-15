def get_new_notes(salary,bills):
    tb = sum(bills)
    return int((salary-tb)/5) if salary > tb else 0

