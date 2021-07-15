def multiply(n):
    account = 0
    for value in str(abs(n)):
        account += 1
    return n*(5**account)

