def mango(quantity, price):
    print('==>> ', quantity, price)
    num_3 = int(quantity / 3)
    print('Num_3: ', num_3)
    output = (quantity - num_3) * price
    return output
