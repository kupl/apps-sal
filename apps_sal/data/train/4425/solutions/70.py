def mango(quantity, price):
    groupsOfThree = quantity // 3
    remainder = quantity - groupsOfThree * 3
    return groupsOfThree * price * 2 + remainder * price
