def billboard(name: str, price: int = 30) -> int:
    return sum(price for _ in range(len(name)))

