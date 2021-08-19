def get_order(order):
    return ''.join([item * order.count(item[1:].lower()) for item in ' Burger, Fries, Chicken, Pizza, Sandwich, Onionrings, Milkshake, Coke'.split(',')])[1:]
