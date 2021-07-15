from re import findall

def get_order(order):
    menu = ['Burger','Fries','Chicken','Pizza','Sandwich','Onionrings','Milkshake','Coke']
    return ' '.join(filter(None, (' '.join(findall(item.lower(), order)).title() for item in menu)))
