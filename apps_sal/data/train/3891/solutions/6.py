def get_new_notes(salary, bills):
    balance = salary - sum(bills)
    return 0 if balance <= 0 else balance // 5
