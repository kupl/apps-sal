def tax_calculator(total):
    if not isinstance(total, (int, float)) or total < 0:
        return 0
    tax = 0
    if total > 30:
        tax = 2.2 + (total - 30) * 0.03
    elif total > 20:
        tax = 1.7 + (total - 20) * 0.05
    elif total > 10:
        tax = 1 + (total - 10) * 0.07
    elif total > 0:
        tax = total / 10.0
    return round(tax, 2)
