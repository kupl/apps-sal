def percentage(value, percent):
    return value * percent / 100

def calculate_total(subtotal, tax, tip):
    total = subtotal + percentage(subtotal, tax) + percentage(subtotal, tip)
    return round(total, 2)

