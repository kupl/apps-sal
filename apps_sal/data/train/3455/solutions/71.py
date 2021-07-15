def disarium_number(number: int) -> str:
    return "Disarium !!" if number == sum(int(a) ** i for i, a in enumerate(str(number), 1)) else "Not !!"

