def tax_calculator(total):
    tax = 0
    if type(total) in (float, int) and total > 0:
        for (limit, rate) in ((30, 3), (20, 5), (10, 7), (0, 10)):
            if total > limit:
                tax += rate * (total - limit)
                total = limit
    return round(tax) / 100
