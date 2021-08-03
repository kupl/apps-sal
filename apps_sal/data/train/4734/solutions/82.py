def bonus_time(salary, bonus):
    if not bonus:
        return f"${salary}"
    else:
        return f"${salary * 10}"
