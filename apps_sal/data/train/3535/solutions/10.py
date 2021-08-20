def get_order(order):
    word = ''
    list = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    for i in list:
        word = word + (' ' + i) * order.count(i.lower())
    return word.strip()
