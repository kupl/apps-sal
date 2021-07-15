def digits(n):
    print(type(n))
    if isinstance(n, int):
        return len(str(n))
    
    return 0
