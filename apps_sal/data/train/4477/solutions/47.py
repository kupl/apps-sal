def reverse_number(n):

    x = ""

    if n < 0:
        x += "-"

    n = abs(n)
    n = str(n)
    n = n[::-1]
    x += n

    x = int(x)
    return x
