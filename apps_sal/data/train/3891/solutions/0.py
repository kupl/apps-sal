def get_new_notes(salary, bills):
    return max((salary - sum(bills)), 0) // 5
