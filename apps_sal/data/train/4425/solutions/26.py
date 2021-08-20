def mango(quantity, price):
    non_discounted_mangos = quantity % 3
    discounted_mangos = quantity - non_discounted_mangos
    return discounted_mangos / 3 * 2 * price + non_discounted_mangos * price
