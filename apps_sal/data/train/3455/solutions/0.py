def disarium_number(n):
    return "Disarium !!" if n == sum(int(d)**i for i, d in enumerate(str(n), 1)) else "Not !!"
