def process_data(data):
    from numpy import prod, sum
    return prod([el1 - el2 for el1, el2 in data])
