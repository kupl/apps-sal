def get_new_notes(salary, bills):
    disposable_income = salary - sum(bills)
    return max(disposable_income // 5, 0)
