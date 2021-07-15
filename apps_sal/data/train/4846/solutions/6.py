def calculate_total(subtotal, tax, tip):
    return round(subtotal + tax / 100 * subtotal + tip / 100 * subtotal, 2)
