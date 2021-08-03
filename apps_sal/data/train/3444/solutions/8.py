def cyclic_string(st):
    for x in range(1, len(st) + 1):
        aux = st[:x] * len(st)
        if aux.startswith(st):
            break
    return x
