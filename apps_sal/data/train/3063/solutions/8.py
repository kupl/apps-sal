from statistics import mean
regular = 'Banana Orange Apple Lemon Grapes'
special = 'Avocado Strawberry Mango'
extra = ''
menu = {regular: 5, special: 7, extra: 9}
prices = {juice: price for (juices, price) in menu.items() for juice in juices.split()}


def mix_fruit(order):
    return round(mean((prices.get(juice.title(), menu[extra]) for juice in order)))
