def calculate_total(subtotal, tax, tip):
    return round(subtotal * (1 + tax / 100.0 + tip / 100.0), 2)
