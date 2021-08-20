rates = ((30, 0.03), (20, 0.05), (10, 0.07), (0, 0.1))


def tax_calculator(total):
    if type(total) in (int, float) and total > 0:
        amount = 0
        for (limit, rate) in rates:
            if total > limit:
                amount += (total - limit) * rate
                total = limit
        return round(amount, 2)
    return 0
