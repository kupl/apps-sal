def mango(quantity, price):
    total = 0
    for each in range(1,quantity +1):
        if each % 3 != 0:
            total += price
    return total

