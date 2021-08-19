def calculate_total(subtotal, tax, tip):
    tax = tax / 100.0 * subtotal
    tip = tip / 100.0 * subtotal
    return round(subtotal + tip + tax, 2)
