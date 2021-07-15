def split_exp(n):
    integer, decimal = n.split(".") if ("." in n) else (n, "")
    length = len(integer)
    result = [d.ljust(length - i, "0") for i, d in enumerate(integer) if int(d)]
    if decimal:
        result.extend("." + d.rjust(i, "0") for i, d in enumerate(decimal, 1) if int(d))
    return result
