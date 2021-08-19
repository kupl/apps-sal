def tax_calculator(total):
    if type(total) not in [int, float] or total < 0:
        return 0
    if total <= 10:
        tax = 0.1 * total
    elif total <= 20:
        tax = 1 + 0.07 * (total - 10)
    else:
        tax = 1.7 + 0.05 * min(total - 20, 10)
        if total > 30:
            tax += 0.03 * (total - 30)
    return round(tax, 2)
