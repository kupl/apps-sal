def tax_calculator(total):
    try:
        total = max(float(total), 0)
    except (AttributeError, TypeError, ValueError):
        total = 0
    tax = 0
    for rate, limit in [(0.1, 10), (0.07, 10), (0.05, 10), (0.03, 99999999999999)]:
        tax += min(total, limit) * rate
        total -= limit
        if total <= 0:
            break
    return round(tax, 2)
