def mango(quantity, price):
    paid_mangos = (quantity - quantity % 3) // 3 * 2 + quantity % 3
    return paid_mangos * price
