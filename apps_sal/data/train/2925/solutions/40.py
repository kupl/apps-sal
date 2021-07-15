def multiply(n):
    return 5 ** len(str(n)[1:]) * n if str(n).startswith('-') else 5 ** len(str(n)) * n
