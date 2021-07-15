import re

MENU = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']

def get_order(order):
    res = []
    for item in MENU:
        res.extend(re.findall(item, order))
    return ' '.join([item.capitalize() for item in res])
