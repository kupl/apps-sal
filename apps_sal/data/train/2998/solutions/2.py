from numpy import roots

def atomic_number(electrons):
    root = roots((2, 3, 1, -3*electrons))[2].real
    full = int(root)
    result = [2*n*n for n in range(1, full+1)]
    if root%1: result.append(electrons - full*(full+1)*(2*full+1)//3)
    return result
