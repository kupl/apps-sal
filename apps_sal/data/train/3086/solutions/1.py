def unflatten(flat):
    if not flat:
        return []
    if flat[0] < 3:
        return [flat[0]] + unflatten(flat[1:])
    else:
        return [flat[0:flat[0]]] + unflatten(flat[flat[0]:])
