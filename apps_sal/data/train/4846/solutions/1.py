def calculate_total(subtotal, tax, tip):
    return round((1 + (tip + tax) / 100.0) * subtotal, 2)
