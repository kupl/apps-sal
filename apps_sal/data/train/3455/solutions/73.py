def disarium_number(n):
    return "Disarium !!" if sum(int(x) ** i for i,x in enumerate(str(n),1)) == n else 'Not !!'
