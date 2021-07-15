def mango(quantity, price):
    grupos = quantity//3
    residuo = quantity%3
    precio = (grupos*2 * price)

    if residuo == 0:
        return precio
    elif residuo == 1:
        return precio+price
    elif residuo == 2:
        return precio+(price*2)
