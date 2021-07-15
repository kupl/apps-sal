def get_order(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    clean_order = ''
    for i in menu:
        clean_order += (i.capitalize() + ' ') * order.count(i)
    return clean_order[:-1]
