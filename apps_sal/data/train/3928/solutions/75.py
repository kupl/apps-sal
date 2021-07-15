from numpy import prod

def billboard(name, price=30):
    return prod([len(name),price])
