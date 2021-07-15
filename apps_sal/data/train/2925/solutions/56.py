def multiply(n):
    if n > 0:
        multiplier = 5 ** len(str(n))
        operation = n * multiplier
        return operation
    else:
        convert = abs(n)
        mn = 5 ** len(str(convert))
        on = n * mn
        return on

