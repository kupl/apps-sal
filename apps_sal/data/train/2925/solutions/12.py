def multiply(n):
    # your code here
    return n * 5 ** len([i for i in str(n) if i.isdigit()])
