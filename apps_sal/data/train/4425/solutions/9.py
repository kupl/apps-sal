def mango(quantity: int, price: int) -> int:
    """
    Calculate the total cost of the mangoes for a given quantity and price.
    Rule: "3 for 2" (or "2+1" if you like) offer on mangoes.
    """
    return (quantity - (quantity // 3)) * price
