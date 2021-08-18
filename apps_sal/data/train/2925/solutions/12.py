def multiply(n):
    return n * 5 ** len([i for i in str(n) if i.isdigit()])
