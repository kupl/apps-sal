get_order = lambda order: "".join([item*order.count(item[1:].lower()) for item in " Burger, Fries, Chicken, Pizza, Sandwich, Onionrings, Milkshake, Coke".split(',')])[1:]
