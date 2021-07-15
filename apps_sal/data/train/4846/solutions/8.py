def calculate_total(subtotal, tax, tip):
    return round(subtotal * (100 + tip + tax) / 100, 2)
