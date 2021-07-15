def productFibAux(current, nxt, prod):
    res = []
    while (current * nxt < prod):
            k = nxt
            nxt = nxt + current
            current = k
    if (prod == current * nxt):
        return [current, nxt, True]
    else:
        return [current, nxt, False]
    return res

def productFib(prod):
    return productFibAux(0, 1, prod)

