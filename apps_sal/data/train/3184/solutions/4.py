def total_bill(s):
    sushi = s.count("r")
    discount = int(sushi / 5)
    sushi -= discount
    return sushi * 2
