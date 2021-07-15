# def mango(quantity, price):
# #     if quantity % 3 == 0:
# #         return (quantity//3)*2*price
# #     # if quantity % 3 == 1:
# #     else:
# #         return ((quantity//3)*2 + 1)*price
def mango(quantity, price):
    return (quantity - quantity // 3) * price
