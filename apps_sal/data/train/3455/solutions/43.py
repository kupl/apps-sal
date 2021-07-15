def disarium_number(n):
    return "Disarium !!" if sum([int(str(n)[x])**(x+1) for x in range(len(str(n)))]) == n else "Not !!"
