def multiply(n):
    
    copy = str(n)
    length = len(copy)
    if n < 0:
        length = length - 1
    return n * (5**length)
