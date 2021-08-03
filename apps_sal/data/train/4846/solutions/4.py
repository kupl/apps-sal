def calculate_total(subtotal, tax, tip):
    return float("{0:.2f}".format(subtotal + subtotal * (tax + tip) / 100))
