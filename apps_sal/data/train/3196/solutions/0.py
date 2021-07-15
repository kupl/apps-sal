def triangular_range(start, stop):
    return {i:i*(i+1)/2 for i in range(stop) if start <= i*(i+1)/2 <= stop}

