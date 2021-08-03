def get_new_notes(salary, bills):
    return max(0, (salary - sum(bills)) // 5)
