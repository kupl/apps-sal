def triangular_range(start, stop):
    
    return {n: n * (n + 1) // 2 for n in range(int(start ** .5), stop) if start <= n * (n + 1) // 2 <= stop}
