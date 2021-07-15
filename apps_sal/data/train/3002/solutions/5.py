pronics = {i * (i+1) for i in range(1000)}

def is_pronic(n):
    return n in pronics
