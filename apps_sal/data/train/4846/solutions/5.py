def calculate_total(subtotal, tax, tip):
    meal = subtotal*(1+(tax+tip)/100)
    return round(meal,2)
