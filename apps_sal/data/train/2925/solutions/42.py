def multiply(n):
    if n<0:
        n = n*(-1)
        return -(5**len(str(n))*n)
    return (5**len(str(n))*n)
