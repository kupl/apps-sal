def multiply(n):
    # your code here
    return n * 5 ** len(list(filter(str.isdigit, str(n))))
