def get_new_notes(salary, bills):
    remaining = (salary - sum(bills)) // 5
    return remaining if remaining > 0 else 0
    

