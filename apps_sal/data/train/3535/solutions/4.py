import re
MENU = {v: i for (i, v) in enumerate('Burger Fries Chicken Pizza Sandwich Onionrings Milkshake Coke'.split())}
REG_CMD = re.compile('|'.join(MENU), flags=re.I)


def get_order(order):
    return ' '.join(sorted(map(str.title, REG_CMD.findall(order)), key=MENU.get))
