def calculate_total(subtotal, tax, tip):
    tax = tax/100 * subtotal
    tip = tip/100 * subtotal
    return round(subtotal + tax + tip, 2)
