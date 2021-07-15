def calculate_total(subtotal, tax, tip):
    tax = (tax/100.00) * subtotal
    tip = (tip/100.00) * subtotal
    return round(subtotal + tip + tax, 2)
